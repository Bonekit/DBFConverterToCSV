#   Author:         Tobias Menzel
#   Date:           17.08.2018
#   Description:    DBFConverterToCSV to convert .dbf file(s) in .csv.

#   important modules for the DBFConverter.
from dbfread import DBF
import pandas as pd
import os
import csv
import sys

#   Put all .dbf files in the input path, after converting all .csv files will be in the output path.
input_path = "C:/Temp/Input/"
output_path = "C:/Temp/Output/"

#   Every string in the DBFConvert. Translation is much easier.
#   Only one Text String left in the main area.
welcome = "Moin Moin, willkommen im .dbf Converter Tool."
welcome2 = "Dieses Tool arbeitet automatisch, bitte warten Sie einfach."
enter_to_progress = "Beliebige Taste zum fortfahren drücken..."
please_wait = "Bitte warten..."
nothing_found = "Es konnte keine .dbf Datei gefunden werden."
done = "Fertig..."

#   Clear Screen.
clear = lambda: os.system('cls')

#   Main Area.
clear() # Clear console screen.
print(welcome)
print(welcome2)
input(enter_to_progress)
clear() # Clear console screen.
print(please_wait)
for dirpath, dirname, filenames in os.walk(input_path):
    for filename in filenames:
        if filename.endswith(".DBF"):
            print(f"\tUmwandeln von {filename} zu .csv") 
            table = DBF(dirpath + filename, encoding="latin1")
            df = pd.DataFrame(iter(table)) 
            csv_file = filename[:-4] + ".csv" # remove last four characters to put .csv at the end.
            output_path_csv= os.path.join(output_path, csv_file)
            df.to_csv(output_path_csv, sep=';')
        else:
            clear()
            print(nothing_found)
            input(enter_to_progress)

print(done)
input(enter_to_progress)