
from datetime import datetime as dt
from glob import glob
import gzip
import os
from src.core.output_writer import OutputWriter


class OnRoadCsvWriter(OutputWriter):
    """ A class to write custom CSV files for On-Road data.
    """

    COLUMNS = {'co': 0, 'nox': 1, 'sox': 2, 'tog': 3, 'pm': 4, 'nh3': 5}
    STONS_2_KG = 907.185

    def __init__(self, config, position):
        super(OnRoadCsvWriter, self).__init__(config, position)
        self.by_region = self.config.getboolean('Output', 'by_region')
        self.combine = self.config.getboolean('Output', 'combine_regions')
        self.version = self.config['Output']['inventory_version']
        self.grid_file = self.config['GridInfo']['grid_cross_file']
        self.region_names = self.config.eval_file('Misc', 'region_names')
        self.county_to_gai = self.config.eval_file('Output', 'county_to_gai')
        self.gai_to_county = dict((g, c) for c in self.county_to_gai for g in self.county_to_gai[c])
        self.gai_basins = self.config.eval_file('Output', 'gai_basins')
        self.multi_gai_coords = self.config.eval_file('Output', 'multi_gai_coords')

    def write(self, scaled_emissions):
        """ The master method to write output files.
            This can write output files by region, or for the entire day.
        """
        if self.by_region:
            self.write_by_region(scaled_emissions)
        else:
            self.write_by_state(scaled_emissions)

    def write_by_region(self, scaled_emissions):
        """ Write a single file for each region/date combo
        """
        for region, region_data in scaled_emissions.data.iteritems():
            for date, date_date in region_data.iteritems():
                self._write_ocsv_by_region(scaled_emissions, region, date)

    def write_by_state(self, scaled_emissions):
        """ Write a single output file per day
        """
        # find all dates
        dates = set()
        for region, region_data in scaled_emissions.data.iteritems():
            for date in region_data:
                dates.add(date)

        # write a file for each date
        dates = sorted(dates)
        for date in dates:
            self._write_ocsv_by_state(scaled_emissions, date)

    def _write_ocsv_by_state(self, scaled_emissions, date):
        """ Write a single 24-hour OCSV file for a given date, for the entire state.
        """
        out_path = self._build_state_file_path(date)
        lines = []

        # loop through the different levels of the scaled emissions dictionary
        for region, region_data in scaled_emissions.data.iteritems():
            day_data = region_data.get(date, {})
            for hr, hr_data in day_data.iteritems():
                for eic, sparce_emis in hr_data.iteritems():
                    for cell, grid_data in sparce_emis.iteritems():
                        # build list of six pollutants
                        emis = ['', '', '', '', '', '']
                        no_emissions = True
                        for poll, value in grid_data.iteritems():
                            try:
                                col = OnRoadCsvWriter.COLUMNS[poll.lower()]
                            except:
                                # irrelevant pollutant
                                continue
                            val = '{0:.5f}'.format(value * self.STONS_2_KG).rstrip('0')
                            if val != '0.':
                                emis[col] = val
                                no_emissions = False

                        # if there are emissions, build OCSV line
                        if no_emissions:
                            continue
                        lines.append(self._build_ocsv_line(region, hr, eic, cell, emis))

        if lines:
            self._write_zipped_file(out_path, lines)

    def _write_ocsv_by_region(self, scaled_emissions, region, date):
        """ Write a single 24-hour OCSV file for a given region/date combination.
            Each region might have multiple COABDIS, so that has to be worked out.
        """
        out_path = self._build_regional_file_path(region, date)
        lines = []

        for hr, hr_data in scaled_emissions.data[region][date].iteritems():
            for eic, sparce_emis in hr_data.iteritems():
                for cell, grid_data in sparce_emis.iteritems():
                    # build list of six pollutants
                    emis = ['', '', '', '', '', '']
                    no_emissions = True
                    for poll, value in grid_data.iteritems():
                        try:
                            col = OnRoadCsvWriter.COLUMNS[poll.lower()]
                        except:
                            # irrelevant pollutant
                            continue
                        val = '{0:.5f}'.format(value * self.STONS_2_KG).rstrip('0')
                        if val != '0.':
                            emis[col] = val
                            no_emissions = False

                    # if there are emissions, build OCSV line
                    if no_emissions:
                        continue
                    lines.append(self._build_ocsv_line(region, hr, eic, cell, emis))

        self._write_file(out_path, lines)
        self._combine_regions(date)

    def _combine_regions(self, date):
        ''' If all the region files have been written, this will cat them all
            together into one big file.
        '''
        if not self.combine:
            return

        # new output file path
        out_file = self._build_state_file_path(date) + '.gz'

        # use glob to count files in the output folder
        yr, month, day = date.split('-')
        region_paths = os.path.join(self.directory, month, day, '*.ocsv')
        region_files = glob(region_paths)

        # if all regions are finished, zcat results together
        if len(region_files) != len(self.regions):
            return
        print('    + writing: ' + out_file)
        os.system('cat ' + ' '.join(region_files) + ' | gzip -1c > ' + out_file)

        # remove old region files
        os.system('rm ' + ' '.join(region_files) + ' &')

    def _build_ocsv_line(self, region, hr, eic, grid_cell, emis):
        """ Build the complicated OCSV line from available data
            Line Format:
            GAI,EIC14,ROW,COL,HR,EMIS
            69,71074211000000,162,179,7,,,,0.024,
            3,71074211000000,183,190,1,0.015,,,,,
        """
        y, x = grid_cell
        emissions = ','.join(emis)  # TODO: Is this efficient?

        return ','.join([str(region), str(eic), str(y), str(x), str(hr), emissions]) + '\n'

    def _write_zipped_file(self, out_path, lines):
        """ simple helper method to write a list of strings to a gzipped file """
        if not self.combine:
            print('    + writing: ' + out_path + '.gz')

        f = gzip.open(out_path + '.gz', 'wb')
        try:
            f.writelines(lines)
        finally:
            f.close()

    def _write_file(self, out_path, lines):
        """ simple helper method to write a list of strings to a file """
        if not self.combine:
            print('    + writing: ' + out_path)

        f = open(out_path, 'w')
        try:
            f.writelines(lines)
        finally:
            f.close()

    def _build_regional_file_path(self, region, date):
        """ build output file directory and path for OCSV file """
        yr, month, day = date.split('-')

        out_dir = os.path.join(self.directory, month, day)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        nomen = self.region_names[region].replace(')', '').replace('(', '').replace(' ', '_')
        return os.path.join(out_dir, nomen + '.ocsv')

    def _build_state_file_path(self, date):
        """ Build output file directory and path for a daily, multi-region OCSV file.
            NOTE: This method uses an extremely detailed file naming convention.
                  For example:
            st_4k.mv.v0938..2012.203107d18..e14..ocsv
            [statewide]_[4km grid].[mobile source].[version 938]..[base year 2012].
            [model year 2031][month 7]d[day 18]..[EIC 14 categories]..[OCSV format]
        """
        yr, month, day = date.split('-')

        out_dir = os.path.join(self.directory, 'ocsv')
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        # define the grid size string
        grid_size = '4k'
        grid_name = os.path.basename(self.grid_file)
        if '12km' in grid_name:
            grid_size = '12k'
        elif '36km' in grid_name:
            grid_size = '36k'
        elif '1km' in grid_name:
            grid_size = '1k'
        elif '250m' in grid_name:
            grid_size = '250m'

        # TODO: "st" = state, "mv" = mobile, and "e14" = EIC-14 All can change
        file_name = 'st_' + grid_size + '.mv.' + self.version + '..' + str(self.base_year) + '.' + \
                    yr + month + 'd' + day + '..e14..ocsv'

        return os.path.join(out_dir, file_name)
