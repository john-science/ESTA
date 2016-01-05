
from datetime import datetime as dt
import gzip
import os
from county_names import county_names
from split_counties import county_to_gai, gai_basins, multi_gai_coords
from output_writer import OutputWriter


class Pmeds1Writer(OutputWriter):
    """ A class to write PMEDS v1 output files.
        One for each county/date combination.
    """

    COLUMNS = {'co': 0, 'nox': 1, 'sox': 2, 'tog': 3, 'pm': 4, 'nh3': 5}
    STONS_2_KG = 907.185

    def __init__(self, config, directory, time_units):
        super(Pmeds1Writer, self).__init__(config, directory, time_units)
        self.date_format = self.config['Dates']['format']
        self.start_date = dt.strptime(self.config['Dates']['start'], self.date_format)
        self.end_date = dt.strptime(self.config['Dates']['end'], self.date_format)
        self.base_year = int(self.config['Dates']['base_year'])
        self.counties = Pmeds1Writer.parse_counties(self.config['Subareas']['subareas'])
        by_subarea = self.config['Output']['by_subarea'].lower()
        self.by_subarea = False if by_subarea in ['false', '0', 'no'] else True
        self.version = self.config['Misc']['inventory_version']

    def write(self, scaled_emissions):
        """ The master method to write output files.
            In this case, we are writing a single file for each county/date combo.
        """
        if self.by_subarea:
            self.write_by_gai(scaled_emissions)
        else:
            self.write_by_state(scaled_emissions)

    def write_by_gai(self, scaled_emissions):
        """ The master method to write output files.
            In this case, we are writing a single file for each county/date combo.
        """
        for county, county_data in scaled_emissions.data.iteritems():
            for date, date_date in county_data.iteritems():
                self._write_pmeds1_by_county(scaled_emissions, county, date)

    def write_by_state(self, scaled_emissions):
        """ The master method to write output files.
            In this case, we are writing a single file for each county/date combo.
        """
        # find all dates
        dates = set()
        for county, county_data in scaled_emissions.data.iteritems():
            for date in county_data:
                dates.add(date)

        # write a file for each date
        dates = sorted(dates)
        for date in dates:
            self._write_pmeds1_by_state(scaled_emissions, date)

    def _write_pmeds1_by_state(self, scaled_emissions, date):
        """ Write a single 24-hour PMEDS file for a given date, for the entire state.
            Each county might have multiple COABDIS, so that has to be worked out.
        """
        out_path = self._build_state_file_path(date)
        jul_day = dt.strptime(str(self.base_year) + date[4:], self.date_format).timetuple().tm_yday
        lines = []

        # loop through the different levels of the scaled emissions dictionary
        for county, county_data in scaled_emissions.data.iteritems():
            day_data = county_data[date]
            for hr, hr_data in day_data.iteritems():
                for eic, sparce_emis in hr_data.iteritems():
                    for cell, grid_data in sparce_emis.iteritems():
                        # calculate GAI from county and cell
                        gais = self._find_gais(county, cell)
                        # loop over GAIs
                        for gai, frac in gais:
                            # build list of six pollutants
                            emis = ['']*6
                            for poll, value in grid_data.iteritems():
                                if poll.lower() not in Pmeds1Writer.COLUMNS:
                                    continue
                                col = Pmeds1Writer.COLUMNS[poll.lower()]
                                val = '{0:.5f}'.format(value * frac * self.STONS_2_KG).rstrip('0')
                                if val != '0.':
                                    emis[col] = val

                            # if there are emissions, build PMEDS line
                            if not ''.join(emis):
                                continue
                            lines.append(self._build_pmeds1_line(county, gai, date, jul_day, hr,
                                                                 eic, cell, emis))

        self._write_zipped_file(out_path, lines)

    def _write_pmeds1_by_county(self, scaled_emissions, county, date):
        """ Write a single 24-hour PMEDS file for a given county/date combination.
            Each county might have multiple COABDIS, so that has to be worked out.
        """
        out_path = self._build_county_file_path(county, date)
        jul_day = dt.strptime(str(self.base_year) + date[4:], self.date_format).timetuple().tm_yday
        # format: data[hr][eic] = SparceEmissions (sparce_emis[(grid, cell)][pollutant] = value)
        data = scaled_emissions.data[county][date]
        lines = []

        for hr, hr_data in data.iteritems():
            for eic, sparce_emis in hr_data.iteritems():
                for cell, grid_data in sparce_emis.iteritems():
                    # calculate GAI from county and cell
                    gais = self._find_gais(county, cell)
                    # loop over GAIs
                    for gai, frac in gais:
                        # build list of six pollutants
                        emis = ['']*6
                        for poll, value in grid_data.iteritems():
                            if poll.lower() not in Pmeds1Writer.COLUMNS:
                                continue
                            col = Pmeds1Writer.COLUMNS[poll.lower()]
                            val = '{0:.5f}'.format(value * frac * self.STONS_2_KG).rstrip('0')
                            if val != '0.':
                                emis[col] = val

                        # if there are emissions, build PMEDS line
                        if not ''.join(emis):
                            continue
                        lines.append(self._build_pmeds1_line(county, gai, date, jul_day, hr, eic,
                                                             cell, emis))

        self._write_zipped_file(out_path, lines)

    def _build_pmeds1_line(self, cnty, gai, date, jul_day, hr, eic, grid_cell, emis):
        """ Build the complicated PMEDS v1 line from available data
            Line Format:
            Amador                71074211000000162179               3122001313 MC  7     ,,,,0.024,
            Los Ange              71074211000000165180               3122000707 MC  7     ,,,0.008,,
            Alpine                71074211000000183190               2122001414GBV  1     0.015,,,,,
        """
        # define parameters
        yr = date[2:4]
        county = county_names[cnty][:8].ljust(8)
        x, y = grid_cell
        hour = '%02d%02d' % (hr, hr)
        basin = gai_basins[gai].rjust(3)
        emissions = ','.join(emis)

        return county + str(eic).rjust(28) + str(x).rjust(3) + str(y).rjust(3) + \
               '              ' + str(cnty).rjust(2) + yr + str(jul_day).rjust(3) + hour + basin + \
               str(gai).rjust(3) + '     ' + emissions + '\n'

    def _write_zipped_file(self, out_path, lines):
        """ simple helper method to write a list of strings to a file """
        f = gzip.open(out_path + '.gz', 'wb')
        for line in lines:
            f.write(line)
        f.close()

    def _find_gais(self, county, grid_cell):
        """ Find the GAIs related to the given grid cell.
            Since we know the county, this is very easy for the counties that match 1-to-1 with
            a GAI. Otherwise, we have to use a look-up table, by grid cell.
        """
        gai_list = county_to_gai[county]

        if len(gai_list) == 1:
            # For the easy counties
            return [[gai_list[0], 1.0]]
        elif grid_cell in multi_gai_coords[county]:
            # for the multi-GAI counties
            return multi_gai_coords[county][grid_cell]
        else:
            # multi-GAI grid cell not found, use default GAI in county
            return [[gai_list[0], 1.0]]

    def _build_county_file_path(self, county, date):
        """ build output file directory and path for PMEDS file """
        yr, month, day = date.split('-')

        out_dir = os.path.join(self.directory, month, day)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        return  os.path.join(out_dir, county_names[county] + '.pmeds')

    def _build_state_file_path(self, date):
        """ build output file directory and path for PMEDS file
            ex: st_4k.mv.v0938..2012.203107d18..e14..pmeds
        """
        yr, month, day = date.split('-')

        out_dir = os.path.join(self.directory, 'pmeds')
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        file_name = 'st_4k.mv.' + self.version + '..' + str(self.base_year) + '.' +  yr + month + \
                    'd' + day + '..e14..pmeds'

        return  os.path.join(out_dir, file_name)

    @staticmethod
    def parse_counties(counties_str):
        """ Parse the string we get back from the subareas field """
        if '..' in counties_str:
            counties = counties_str.split('..')
            counties = range(int(counties[0]), int(counties[1]))
        else:
            counties = [int(c) for c in counties_str.split()]

        return counties