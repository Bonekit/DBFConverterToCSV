---
Author: Tobias Menzel
Date: 17.08.2018
Licence: 
Language: Python 3.7
---

# DBFConverterToCSV
The DBFConverterToCSV convert all .dbf files to .csv files.  
Not every .dbf file can be converted, but i´ll work on it.
The script will loop over all .dbf files. Is there a not working .dbf file, 
the script will automatically work with the next .dbf file.

# How to use the script?
Copy the script into the path where the .dbf files are. then execute the script via command-line.

# Build with
- Python 3.7

## Known Issues
- Memofile Exception from dbfread at some files.
