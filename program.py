# Title:            DBFConverterToCSV
# Description:      Converte .dbf files to .csv files.
# Author:           Tobias Menzel
# Date:             17.08.2018
# Version:          0.1
# Language:         Python 3.7
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Important modules for the DBFConverter.
import dbfread
import subprocess as sub
import pandas as pd
import os


# Define functions.


def clear():
    """Clear the console screen on windows"""
    sub.call('cls', shell=True)


def main():
    """Main function to convert all .dbf files into .csv files"""
    # Declaration.
    cnt_errors = 0

    # Get the path where the script is. All .dbf files inside this path will be converted into .csv.
    script_path = os.path.dirname(__file__)

    # Clear the console screen.
    clear()

    # Script is starting to find all .dbf files.
    print('Script is searching for .dbf files.')

    # Search for .dbf files inside the script path.
    for dirpath, dirname, filenames in os.walk(script_path):
        for filename in filenames:
            if filename.endswith(".dbf"):
                print("Convert: {filename} to .csv".format(filename=filename))

                # Combine both strings.
                full_path = dirpath + filename

                # Try to load the .dbf file.
                try:
                    table = dbfread.DBF(full_path, encoding="windows-1252", ignore_missing_memofile=False)
                except dbfread.exceptions.DBFNotFound as dbf_exc:
                    print("Error occurred: \n{file} \n{error}".format(file=filename, error=dbf_exc))
                    cnt_errors += 1
                    continue

                # Load data from table into an DataFrame.
                df = pd.DataFrame(iter(table))

                # remove last four characters to put .csv at the end.
                csv_file = filename[:-4] + ".csv"

                # Join the script path.
                output_path_csv = os.path.join(script_path, csv_file)

                # Print the convert message into the console and write all data in a .csv file.
                print("Convert: {filename} to .csv".format(filename=filename))
                df.to_csv(output_path_csv, sep=';')

    # Print out amount of not converted .dbf files.
    print('Amount of not converted files: {}'.format(cnt_errors))


# Application Start.


if __name__ == '__main__':
    main()
