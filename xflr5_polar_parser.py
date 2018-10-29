#!/user/bin/env python3
"""
This script is used to parser XFLR5 polar files.
It has been tested with XFLR5 v6.09.06.

Copyright Rebecca Li 2018
robot@seas.upenn.edu
"""

import argparse
import pandas as pd


def add_dataline_to_dict(data_dict, header_list_raw, dataline):
    """ For each line of data, add the line to the corresponding
        dictionary header.
    """

    # turn the dataline into a list of numbers
    datalist = [float(x) for x in dataline.split()]

    # add it to the right header
    for i, h in enumerate(header_list_raw):
        data_dict[h].append(datalist[i])
    return data_dict


def add_deflection_and_dataline_to_dict(data_dict, header_list_raw, dataline, deflection):
    """ For each line of data, add the line to the corresponding
        dictionary header.
    """
    data_dict['deflection'].append(deflection)
    data_dict = add_dataline_to_dict(data_dict, header_list_raw, dataline)
    return data_dict


def get_deflection(raw_txt):
    """Strips out the deflection from XFLR5 txt file"""
    # Look at the end of the second line
    foil_name = raw_txt[2]
    # remove \n
    foil_name = foil_name[:-1]
    # get the deflection
    deflection = float(foil_name[foil_name.rfind('d')+1:])
    return deflection


def parse_polar(raw_txt):
    """ Parse the polar txt file and return a dictionary.
        Raw_txt should be a list of strings corresponding to lines of
        the file.
    """
    header_str = '  alpha     CL        CD       CDp       Cm    Top Xtr Bot Xtr   Cpmin    Chinge    XCp\n'  # noqa: E501
    header_list_raw = ['alpha', 'CL', 'CD', 'CDp', 'Cm', 'Top Xtr', 'Bot Xtr', 'Cpmin', 'Chinge', 'XCp']
    header_list = header_list_raw[:]
    header_list.append('deflection')
    header_index = raw_txt.index(header_str)
    data_start_index = header_index + 2

    # Make a dictionary with values of empty lists
    data_dict = dict.fromkeys(header_list)
    # initialize with blank list
    for key in data_dict:
        data_dict[key] = []

    # Get the deflection:
    deflection = get_deflection(raw_txt)
    print('deflection %f' % deflection)

    # iterate through all the data
    for i in range(data_start_index, len(raw_txt)):
        if raw_txt[i] is not "\n":
            add_deflection_and_dataline_to_dict(data_dict, header_list_raw, raw_txt[i], deflection)
    return data_dict


def main(args):
    """Main function, takes args.i and args.o"""
    input_file = args.i
    inputfile2 = args.ii
    output_file = args.o

    # Read the file:
    with open(input_file) as f:
        raw_txt = f.readlines()

    data_dictionary = parse_polar(raw_txt)

    with open(inputfile2) as f:
        raw_txt2 = f.readlines()

    data_dictionary2 = parse_polar(raw_txt2)

    df = pd.DataFrame.from_dict(data_dictionary)
    df2 = pd.DataFrame.from_dict(data_dictionary2)
    df = df.append(df2, ignore_index=True)
    df.to_csv(output_file)
    print("Wrote file to %s." % output_file)


# Main body
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert XFLR5 polar from txt to csv.')
    parser.add_argument('-i', type=str, help='input file', default='testPolar.txt')
    parser.add_argument('-ii', type=str, help='input file', default='testPolar.txt')
    parser.add_argument('-o', type=str, help='output file', default='testPolar.csv')
    args = parser.parse_args()
    main(args)
