# IceKitty
Digital Artefact Extractor for TeamSpeak3

Developed as part of my B.Sc. (Hons) Dissertation entitled "Retrieval of Digital Artefacts from TeamSpeak and Discord: A Forensic Investigation and Analysis of the Malicious Use of Gaming Communication Clients"

In citing the use of this tool in any future publications please use the correct citiation "Bryant, O. (2018). Retrieval of Digital Artefacts from TeamSpeak and Discord: A Forensic Investigation and Analysis of the Malicious Use of Gaming Communication Clients."

This script can be used to automate the extraction of localizsed data from the TeamSpeak3 local client databases into a readable CSV format.


## The Findings
During the dissertation study a file called "settings.db" was discovered in the AppData/TS3Client folder, this database included how many times files had been uploaded and downloaded using the client.
The second file found in the same folder called "urls.db" contains a list of URLs clicked on by the client.



## Installation Guide
This script has been run and tested with Python3 only, If you do not have a copy of Python3 on your machine please visit python.org and download a fresh copy.
In addition the script also requires the third party python package "Another Python SQLite wrapper" also known as "apsw". 

Simply run "pip install apsw" to get this package.

## User Guide
In order to extract the user settings/urls databases you must have a copy of the settings.db and urls.db file. These can be found at the following folder directory "C:\Users\USERNAME\AppData\Roaming\TS3Client".

Once you have a copy of the file on your local machine you can run this example command.
python3 icekitty.py -u urls.db -o urls.csv

This will generate a CSV of the data found in the urls.csv database.

In order to do the same with the settings.db simply switch the arguments from -u to -s, for example

python3 icekitty.py -s settings.db -o settings.csv

To view all the flags available run the -h command.


## Disclosure
This tool is for RESEARCH PURPOSES ONLY! Use with caution. 



## Licence
This tool is licenced under MIT License.

## With Thanks
I wish to thank the following people who helped me during my Dissertation.
- Giri, Chris, Nicki, Peter, Dan, Peter, Clare and Sophie
- Ms. Georgina Humphries
- Mr. Danny Webb
- Dr. Ian Kennedy
- Canterbury Christ Church University, School of Law, Criminal Justice and Computing
- Thanks also goes out to Discord LLC and TeamSpeak GmBH for providing me the original goahead for the development of these tools.
