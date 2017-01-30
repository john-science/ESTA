
from datetime import datetime
from glob import glob
import gzip
from netCDF4 import Dataset
import os
import shutil
from src.core.output_tester import OutputTester
from src.core.eic_utils import eic_reduce


class Emfac2014TotalsTester(OutputTester):

    KG_2_STONS = 0.001102310995
    MOLESEC2KG = 3600.0 * KG_2_STONS
    SUMMER_MONTHS = [4, 5, 6, 7, 8, 9]
    POLLUTANTS = ['CO', 'NOX', 'SOX', 'TOG', 'PM']

    def __init__(self, config, position):
        super(Emfac2014TotalsTester, self).__init__(config, position)
        self.by_region = self.config.getboolean('Output', 'by_region')
        self.combine = self.config.getboolean('Output', 'combine_regions') if self.by_region else False
        self.vtp2eic = self.config.eval_file('Misc', 'vtp2eic')
        self.region_names = self.config.eval_file('Misc', 'region_names')
        self.emis_dirs = self.config.getlist('Emissions', 'emissions_directories')
        self.reverse_region_names = dict(zip(self.region_names.values(), self.region_names.keys()))
        self.weight_file = ''
        self.groups = {}
        # default to EIC3 (particularly for NetCDF)
        if 'eic_precision' in self.config['Output']:
            self.eic_reduce = eic_reduce(self.config['Output']['eic_precision'])
        else:
            self.eic_reduce = eic_reduce('3')

    def test(self):
        ''' Master Testing Method. This method compares the final PMEDS/NetCDF output file emissions
            to the original EMFAC2014 input files.
            PMEDS files will by compared by county and date, but NetCDF files will only be compared
            by date.

            NOTE BENE: If the date tested is not a Tues/Wed/Thurs, the emissions will not be the
                       same as the EMFAC totals, as EMFAC represents only the "typical work day".
        '''
        # if no testing dates are provided, test all days in run
        if not self.dates:
            self._find_dates_in_range()

        # loop through each date
        for date in self.dates:
            dt = datetime.strptime(date, self.date_format)
            emis = {}

            # for each region
            for region_num in self.regions:
                #   sum the input LDV EMFAC 2014 emissions
                ldv_file = self._find_emfac2014_ldv(dt, region_num)
                if not ldv_file:
                    continue
                emis[region_num] = self._read_emfac2014_ldv(ldv_file, region_num)

            # sum HDV EMFAC 2014 emissions
            hdv_file = self._find_emfac2014_hdv(dt)
            if not hdv_file:
                continue
            emis = self._read_emfac2014_hdv(hdv_file, emis)

            # test output pmeds, if any
            pmeds_files = self._find_output_pmeds(dt)
            if pmeds_files:
                self._read_and_compare_txt(pmeds_files, date, emis, 'pmeds')

            # test output netcdf, if any
            ncf_files = self._find_output_ncf(dt)
            if ncf_files:
                self._read_and_compare_ncf(ncf_files, date, emis)

    def _read_and_compare_ncf(self, ncf_files, date, emis):
        ''' Read the output NetCDF files and compare the results with the
            input EMFAC2014 emissions.
        '''
        if not ncf_files or 'weight_file' not in self.config['Output']:
            return

        # if NetCDF file exists, we need the weight file.
        self.weight_file = self.config['Output']['weight_file']

        # sum up emissions in output NetCDF
        out_emis = {}

        # load molecular weights file
        self._load_weight_file()
        for ncf_file in ncf_files:
            out_emis = self._sum_output_ncf(ncf_file, out_emis)

        # write the emissions comparison to a file
        self._write_general_comparison(date, emis, out_emis)

    def _read_and_compare_txt(self, files, date, emis, file_type):
        ''' Read the output PMEDS files and compare the results with the
            input EMFAC2014 emissions.
        '''
        if not files:
            return

        # sum up emissions in output PMEDS
        out_emis = {}
        for f in files:
            if file_type == 'pmeds':
                out_emis = self._sum_output_pmeds(f, out_emis)
            else:
                print('    + File Type Not Found: ' + file_type)

        # write the emissions comparison to a file
        self._write_full_comparison(date, emis, out_emis, file_type)

    def _write_general_comparison(self, date, emfac_emis, ncf_emis):
        ''' Write a quick CSV to compare the EMFAC2014 and final output NetCDF.
            The NetCDF will only allow us to write the difference by pollutant.
            NOTE: Won't print any numbers with zero percent difference.
        '''
        if not os.path.exists(self.testing_dir):
            os.mkdir(self.testing_dir)
        file_path = os.path.join(self.testing_dir, 'ncf_test_' + date + '.csv')
        f = open(file_path, 'w')
        f.write('Pollutant,EMFAC,NetCDF,Percent Diff\n')

        # create all-region EMFAC totals
        emfac_totals = {'CO': 0.0, 'NOX': 0.0, 'SOX': 0.0, 'TOG': 0.0, 'PM': 0.0}
        for region in self.regions:
            if region not in emfac_emis:
                continue
            region_data = emfac_emis[region]
            for eic_data in region_data.itervalues():
                for poll, value in eic_data.iteritems():
                    if poll.upper() in emfac_totals:
                        emfac_totals[poll.upper()] += value

        # find diff between EMFAC and NetCDF & add to file
        for poll in emfac_totals:
            emfac_value = emfac_totals[poll]
            if poll not in ncf_emis:
                ncf_value = 0.0
                if not emfac_value:
                    diff = 0.0
                else:
                    diff = 100.00
            else:
                ncf_value = ncf_emis[poll]
                if not emfac_value:
                    diff = -100.0
                else:
                    diff = Emfac2014TotalsTester.percent_diff(emfac_value, ncf_emis[poll])

            line = [poll, str(emfac_value), str(ncf_value), '%.3f' % diff]
            f.write(','.join(line) + '\n')

        f.close()

    def _write_full_comparison(self, date, emis, out_emis, file_type):
        ''' Write a quick CSV to compare the EMFAC2014 and final output PMEDS.
            Write the difference by region, EIC, and pollutant.
            NOTE: Won't print any numbers with zero percent difference.
        '''
        if not os.path.exists(self.testing_dir):
            os.mkdir(self.testing_dir)
        file_path = os.path.join(self.testing_dir, file_type + '_test_' + date + '.csv')
        f = open(file_path, 'w')
        f.write('Region,EIC,Pollutant,EMFAC,' + file_type.upper() + ',Percent Diff\n')

        total_totals = {'emfac': {'CO': 0.0, 'NOX': 0.0, 'SOX': 0.0, 'TOG': 0.0, 'PM': 0.0},
                        'final': {'CO': 0.0, 'NOX': 0.0, 'SOX': 0.0, 'TOG': 0.0, 'PM': 0.0}}
        for region_num in self.regions:
            region_totals = {'emfac': {'CO': 0.0, 'NOX': 0.0, 'SOX': 0.0, 'TOG': 0.0, 'PM': 0.0},
                             'final': {'CO': 0.0, 'NOX': 0.0, 'SOX': 0.0, 'TOG': 0.0, 'PM': 0.0}}
            c = self.region_names[region_num]
            # write granular totals, by EIC
            eics = set(emis[region_num].keys() + out_emis[region_num].keys())
            for eic in eics:
                for poll in self.POLLUTANTS:
                    # get data
                    emfac = emis.get(region_num, {}).get(eic, {}).get(poll, 0.0)
                    final = out_emis.get(region_num, {}).get(eic, {}).get(poll, 0.0)
                    diff = Emfac2014TotalsTester.percent_diff(emfac, final)
                    # fill region totals
                    region_totals['emfac'][poll] += emfac
                    region_totals['final'][poll] += final
                    # don't write the detailed line if there's no difference
                    if abs(diff) < 1.0e-3:
                        continue
                    diff = '%.3f' % diff
                    f.write(','.join([c, str(eic), poll, str(emfac), str(final), diff]) + '\n')

            # write region totals, without EIC
            for poll in self.POLLUTANTS:
                # write line
                emfac = region_totals['emfac'][poll]
                final = region_totals['final'][poll]
                diff = Emfac2014TotalsTester.percent_diff(emfac, final)
                diff = '%.3f' % diff
                f.write(','.join([c, 'TOTAL', poll, str(emfac), str(final), diff]) + '\n')
                # build statewide totals
                total_totals['emfac'][poll] += emfac
                total_totals['final'][poll] += final

        # if more than one region, write state totals, without EIC
        if len(self.regions) > 1:
            for poll in self.POLLUTANTS:
                emfac = total_totals['emfac'][poll]
                final = total_totals['final'][poll]
                diff = Emfac2014TotalsTester.percent_diff(emfac, final)
                diff = '%.3f' % diff
                f.write(','.join(['TOTAL', 'TOTAL', poll, str(emfac), str(final), diff]) + '\n')

        f.close()

    def _sum_output_pmeds(self, file_path, e):
        ''' Look at the final output PMEDS file and build a dictionary
            of the emissions by region and pollutant.
        '''
        if file_path.endswith('.gz'):
            f = gzip.open(file_path, 'rb')
        elif os.path.exists(file_path):
            f = open(file_path, 'r')
        else:
            print('Emissions File Not Found: ' + file_path)
            return e

        # now that file exists, read it
        for line in f.readlines():
            region = int(line[71:73])
            eic = int(line[22:36])
            vals = [float(v) if v else 0.0 for v in line[78:].rstrip().split(',')]

            if region not in e:
                e[region] = {}
            if eic not in e[region]:
                e[region][eic] = dict(zip(self.POLLUTANTS, [0.0]*len(self.POLLUTANTS)))

            for i in xrange(5):
                e[region][eic][self.POLLUTANTS[i]] += vals[i] * self.KG_2_STONS

        return e

    def _sum_output_ncf(self, file_path, e):
        ''' Look at the output NetCDF file and build a dictionary
            of the emissions by pollutant.
        '''
        # initialize emissions dictionary, if necessary
        for species in self.groups:
            group = self.groups[species]['group']
            if group not in e:
                e[group] = 0.0

        # open NetCDF file (if gzip, copy to temp file)
        if file_path.endswith('.gz'):
            unzipped_path = file_path[:-3]
            temp = open(unzipped_path, "wb")
            shutil.copyfileobj(gzip.open(file_path), temp)
            ncf = Dataset(unzipped_path, 'r')
        else:
            ncf = Dataset(file_path, 'r')

        # loop through each variable in NetCDF file
        sortedvar = sorted(ncf.variables)
        for species in sortedvar:
            if species == 'TFLAG':
                continue
            ems = ncf.variables[species][:24].sum() * self.MOLESEC2KG * self.groups[species]['weight']
            group = self.groups[species]['group']

            if group == 'NOX':
                e[group] += ems * self.groups['NO2']['weight'] / self.groups[species]['weight']
            elif group == 'SOX':
                e[group] += ems * self.groups['SO2']['weight'] / self.groups[species]['weight']
            else:
                # PM, TOG, CO, & NH3
                e[group] += ems

        ncf.close()
        if file_path.endswith('.gz'):
            os.remove(unzipped_path)
        return e

    def _load_weight_file(self):
        """ load molecular weight file
            File Format:
            NO          30.006      NOX    moles/s
            NO2         46.006      NOX    moles/s
            HONO        47.013      NOX    moles/s
        """
        # read molecular weight text file
        fin = open(self.weight_file, 'r')
        lines = fin.read()
        fin.close()

        # read in CSV or Fortran-formatted file
        lines = lines.replace(',', ' ')
        lines = lines.split('\n')

        self.groups = {}
        # loop through file lines and
        for line in lines:
            # parse line
            columns = line.rstrip().split()
            if not columns:
                continue
            species = columns[0].upper()
            self.groups[species] = {}
            self.groups[species]['weight'] = float(columns[1]) / 1000.0
            self.groups[species]['group'] = columns[2].upper()
            self.groups[species]['units'] = columns[3]

    def _find_output_pmeds(self, dt):
        ''' Find the output PMEDS file(s) for a given day. '''
        files = []
        if self.by_region and not self.combine:
            file_str = os.path.join(self.out_dir, '%02d' % dt.month, '%02d' % dt.day, '*.pmed*')
            possibles = glob(file_str)
            if possibles:
                files += possibles
        else:
            date_str = str(dt.month) + 'd' + '%02d' % dt.day
            file_str = os.path.join(self.out_dir, 'pmeds', '*' + date_str + '*.pmed*')
            possibles = glob(file_str)
            if possibles:
                files.append(possibles[0])

        return files

    def _find_output_ncf(self, dt):
        ''' Find the output NetCDF file(s) for a given day. '''
        files = []
        date_str = str(dt.year) + str(dt.month).zfill(2) + 'd' + str(dt.day)
        file_str = os.path.join(self.out_dir, 'ncf', '*' + date_str + '*')
        files += glob(file_str)

        return files

    def _find_emfac2014_ldv(self, dt, region_num):
        ''' Find a single region EMFAC2014 LDV emissions file for a given day. '''
        files = []
        region = self.region_names[region_num].split(' (')[0].replace(' ', '_')
        for edir in self.emis_dirs:
            file_str = os.path.join(edir, '%02d' % dt.month, '%02d' % dt.day, 'emis', region + '.*')
            files += glob(file_str)

        files = filter(lambda f: 'pmeds' not in f[-16:], files)

        if not files:
            print('\tERROR: EMFAC2014 LDV emissions file not found for region: ' + str(region) +
                  ', and date: ' + str(dt))
            return []

        return files[0]

    def _find_emfac2014_hdv(self, dt):
        ''' Find a single EMFAC2014 HDV emissions file for a given day. '''
        season = 'summer' if dt.month in self.SUMMER_MONTHS else 'winter'
        files = []
        for edir in self.emis_dirs:
            file_str = os.path.join(edir, 'hd_' + season, 'emfac_hd_*.csv_all')
            files += glob(file_str)

        if not files:
            print('\tERROR: EMFAC2014 HDV emissions file not found for date: ' + str(dt))
            return []

        return files[0]

    def _read_emfac2014_ldv(self, file_path, region_num):
        """ Read an EMFAC2014 LDV CSV emissions file and colate the data into a table.
            File Format:
            year,month,sub_area,vehicle_class,process,cat_ncat,pollutant,emission_tons_day
            2031,7,Alpine (GBV),LDA,DIURN,CAT,TOG,0.000381882098646
            2031,7,Alpine (GBV),LDA,HOTSOAK,CAT,TOG,0.00171480645826
            2031,7,Alpine (GBV),LDA,PMBW,CAT,PM,0.00472484086652
        """
        e = {}

        # check that the file exists
        if file_path.endswith('.gz'):
            f = gzip.open(file_path, 'rb')
        elif os.path.exists(file_path):
            f = open(file_path, 'r')
        else:
            print('\tERROR: LDV Emissions File Not Found: ' + file_path)
            return e

        region_name = self.region_names[region_num]

        # now that file exists, read it
        header = f.readline()
        for line in f.readlines():
            ln = line.strip().split(',')
            poll = ln[6].upper()
            if poll not in self.POLLUTANTS:
                continue
            if not ln[2].startswith(region_name):
                continue
            v = ln[3]
            t = ln[5]
            if v == 'SBUS' and t == 'DSL':
                # There is no such thing as Light-Duty, Diesel School Busses.
                continue
            p = ln[4]
            eic = self.eic_reduce(self.vtp2eic[(v, t, p)])
            value = float(ln[-1])
            if not value:
                continue
            if eic not in e:
                e[eic] = dict(zip(self.POLLUTANTS, [0.0]*len(self.POLLUTANTS)))
            e[eic][poll] += value

        f.close()
        return e

    def _read_emfac2014_hdv(self, file_path, emis):
        """ Read an EMFAC2014 HD Diesel CSV emissions file and colate the data into a table
            File Format:
            2031,Santa Barbara (SCC),6.27145245709e-08,IDLEX,T6 CAIRP heavy,TOG
            2031,Santa Barbara (SCC),9.39715480515e-05,PMTW,T7 NNOOS,PM10
            2031,Santa Barbara (SCC),2.51918142645e-06,RUNEX,T7 POAK,SOx
        """
        # check that the file exists
        if file_path.endswith('.gz'):
            f = gzip.open(file_path, 'rb')
        elif os.path.exists(file_path):
            f = open(file_path, 'r')
        else:
            print('\tERROR: Emissions File Not Found: ' + file_path)
            return emis

        # now that file exists, read it
        f = open(file_path, 'r')
        for line in f.readlines():
            ln = line.strip().split(',')
            poll = ln[-1].upper()
            if poll not in self.POLLUTANTS:
                continue
            value = float(ln[2])
            if not value:
                continue
            try:
                region = self.reverse_region_names[ln[1]]
            except:
                region = int(ln[1])
            v = ln[4]
            p = ln[3]
            eic = self.eic_reduce(self.vtp2eic[(v, 'DSL', p)])
            if region not in emis:
                emis[region] = {}
            if eic not in emis[region]:
                emis[region][eic] = dict(zip(self.POLLUTANTS, [0.0]*len(self.POLLUTANTS)))
            emis[region][eic][poll] += value

        f.close()
        return emis

    @staticmethod
    def percent_diff(a, b):
        ''' Find the percent difference of two numbers,
            and correctly trap the zero cases.
        '''
        if not a:
            if not b:
                return 0.0
            else:
                return -100.00

        return 100.0 * (a - b) / a
