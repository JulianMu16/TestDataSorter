
# Your name:
# Your student id:
# Your email:
# List who you have worked with on this project:

import io
import sys
import csv
import unittest

def load_csv(filename):
    '''
    Reads in the csv, removes the header (first row) and
    stores the data in the following nested dictionary format:
    {'region': {'race/ethnicity': count...}...}

    Parameters
    ----------
    filename: string
        the file to read

    Returns
    -------
    data: dict
        a nested dictionary
    '''
    data={}

def calc_pct(data):
    '''
    Calculates the percentage of each demographic using this
    formula: (demographic / total people) * 100

    Parameters
    ----------
    data: dict
        Either SAT or Census data

    Returns
    -------
    pcts: dict
        the dictionary that represents the data in terms of percentage share
        for each demographic for each region in the data set
    '''
    pcts = {}

def calc_diff(sat_dict, census_dict):
    '''
    Takes the absolute value, rounded to 2 decimal places,
    of the difference between each demographic's percentage
    value in census_dict from sat_dict

    Parameters
    ----------
    sat_dict: dict
        SAT data
    census_dict: dict
        Census data

    Returns
    -------
    pct_dif: dict
        the dictionary of the percent differences
    '''
    pct_dif = {}

def write_csv(data, file_name):
    '''
    Writes the data to csv, adding the header as
    the first row

    Parameters
    ----------
    data: dict
        dictionary with percent differences

    file_name: str
        the name of the file to write

    Returns
    -------
        None. (Doesn't return anything)
    '''
    pass

def min_max_mutate(data, col_list):
    # Do not change the code in this function
    '''
    Mutates the data to simplify the implementation of
    `min_max` by moving the race/ethnicity key to the outside
    of the nested dictionary and the region key to the inside
    nested dictionary like so:
    {'race/ethnicity': {'region': pct, 'region': pct, ...}...}

    Parameters
    ----------
    data : dict
        dictionary of data passed in.
    col_list : list
        list of columns to mutate to.

    Returns
    -------
    demo_vals: dict
    '''
    # Do not change the code in this function
    demo_vals = {}
    for demo in col_list:
        demo_vals.setdefault(demo, {})
        for region in data:
            demo_vals[demo].setdefault(region, data[region][demo])
    return demo_vals

def min_max(data):
    '''
    Finds the max and min regions and vals for each demographic,
    filling a dictionary in the following format:
    {"min": {"demographic": {"region": value}, ...},
     "max": {"demographic": {"region": value}, ...}...}

    Parameters
    ----------
    data: dict
        the result of min_max_mutate

    Returns
    -------
    min_max: dict
        a triple nested dictionary
    '''
    min_max = {"min":{},"max":{}}

def nat_pct(data, col_list):
    '''
    EXTRA CREDIT
    Uses either SAT or Census data dictionaries
    to sum demographic values, calculating
    national demographic percentages from regional
    demographic percentages

    Parameters
    ----------
    data: dict
        Either SAT or Census data
    col_list: list
        list of the columns to loop through. helps filter out region totals columns

    Returns
    -------
    data_totals: dict
        dictionary of the national demographic percentages

    '''
    data_totals = {}

def nat_diff(sat_data, census_data):
    '''
    EXTRA CREDIT
    Calculates the difference between SAT and Census
    data on a national scale

    Parameters
    ----------
    sat_data: dict
        national SAT data
    census_data: dict
        national Census data

    Returns
    nat_difference: dict
        the dictionary consisting of the demographic
        difference on national level
    '''
    nat_difference = {}

def main():
    '''
    Fill out main per the comments below; 
    You don't have to print anything here, 
    but your code should run write_csv()
    on your computed dict of differences
    '''

    # read in the data

    # compute demographic percentages

    # compute the difference between test taker and state demographics

    # output the csv

    # create a list from the keys of inner dict

    # mutate the data using the provided 'min_max_mutate' function

    # calculate the max and mins using `min_max`

    # print 'min_max' as well 

    # extra credit here

    # if you did the EC, print the dict you get from nat_diff

    pass

main()

# unit testing
class HWTest(unittest.TestCase):

    def setUp(self):
        # surpressing output on unit testing
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        # setting up the data we'll need here
        # basically, redoing all the stuff we did in the main function
        self.sat_data = load_csv("sat_data.csv")
        self.census_data = load_csv("census_data.csv")

        self.sat_pct = calc_pct(self.sat_data)
        self.census_pct = calc_pct(self.census_data)

        self.pct_dif_dict = calc_diff(self.sat_pct, self.census_pct)

        self.col_list = list(self.pct_dif_dict["midwest"].keys())

        self.mutated = min_max_mutate(self.pct_dif_dict, self.col_list)

        self.min_max_val = min_max(self.mutated)

        # extra credit
        # providing a list of col vals to cycle through
        self.col_list = self.census_data["midwest"].keys()

        # computing the national percentages
        self.sat_nat_pct = nat_pct(self.sat_data, self.col_list)
        self.census_nat_pct = nat_pct(self.census_data, self.col_list)

        self.dif = nat_diff(self.sat_nat_pct, self.census_nat_pct)

    '''

    Create test functions for the functions you wrote here!

    '''

    # # testing the nat_pct extra credit function
    # def test_nat_pct(self):
    #    self.assertEqual(
    #    nat_pct({"region":{"demo":5,"Region Totals":10}},["demo", "Region Totals"]),
    #    {'Region Totals': 100.0, 'demo': 50.0})

    # # second test for the nat_pct extra credit function
    # def test2_nat_pct(self):
    #     self.assertEqual(
    #         self.sat_nat_pct["AMERICAN INDIAN/ALASKA NATIVE"],
    #         0.73)

    # # testing the nat_dif extra credit function
    # def test_nat_diff(self):
    #     self.assertEqual(
    #         nat_diff({"demo":0.53, "Region Totals": 1},{"demo":0.5, "Region Totals": 1}),
    #         {'Region Totals': 0, "demo":0.03}
    #         )

    # # second test for the nat_diff extra credit function
    # def test2_nat_diff(self):
    #     self.assertEqual(
    #         self.dif["ASIAN"],
    #         3.32)

if __name__ == '__main__':
    unittest.main(verbosity=2)