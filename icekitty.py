import os, sys, time, apsw, csv
import urllib.parse
import argparse
#print(apsw.sqlitelibversion())
motd = '''
       Kitty Magician
       IceKitty - https://github.com/kittymagician/IceKitty
       Version 1.0 - Developed by Oliver Bryant
       '''
print(motd)
print(" ")
parser = argparse.ArgumentParser()                                               
parser.add_argument("--urls", "-u", type=str, required=False, help="Specify your urls.db file. found in /TS3Client/urls.db")
parser.add_argument("--settings", "-s", type=str, required=False, help="Specify your settings.db found in /TS3Client/settings.db")
parser.add_argument("--output", "-o", type=str, required=False, help="Specify output file eg: -o /directory/file.csv")
args = parser.parse_args()
url = [] # urls.db
timeMentioned = []
lastMentioned = []
mentionedBy = []
timeStamp = [] # settings.db
key = []
value = []
argdis = False

def executesqlsettings():
    argdis = False
    try:
        connection=apsw.Connection(args.settings)
    except:
        exit()
    cursor=connection.cursor()
    try:
        for row in cursor.execute("SELECT * FROM FileTransfer"):
            timeStamp.append(row[0])
            key.append(row[1])
            value.append(row[2])
        try:
            if args.output is None:
                f = open("settingsreport.csv", 'w')
            else:
                f = open(args.output, 'w')
                argdis = True
            with f:
                fnames = ['timestamp', 'key', 'value']
                writer = csv.writer(f)
                writer = csv.DictWriter(f, fieldnames=fnames)
                writer.writeheader()
                maxNum = len(timeStamp)
                counter = 0 
                while counter < maxNum:
                    writer.writerow({'timestamp':timeStamp[counter],'key':key[counter],
                    'value':value[counter]})
                    counter = counter + 1
            f.close()
            if argdis == True:
                print('\x1b[6;30;42m' + 'Exported local TS3 Settings data to ' + args.output + '\x1b[0m')
            else:
                print('\x1b[6;30;42m' + 'Exported local TS3 Settings data to ' + 'settingsreport.csv' + '\x1b[0m')
        except:
            print('\x1b[1;31m'+'ERROR! Unable to open' + args.output + 'are you specifying the correct path?' + '\x1b[0m')
            print('\x1b[1;31m'+'Be sure to specify the ABSOLUTE path. You can use PWD on linux to find the Absolute Path' + '\x1b[0m')
            print('\x1b[1;31m'+'Here\'s an example of a pathway searchcli.py -f file.localstorage -o /home/ubuntu/workspace/test/file.csv'+ '\x1b[0m')
            print('Press ENTER to terminate the application.')
            input()
            exit()
    except:
        print('\x1b[1;31m'+'ERROR! Unable to open SQL file '+ args.urls +'are you specifying the correct http_discordapp.com_0.localstorage file?' + '\x1b[0m')
        print('Press ENTER to terminate the application.')
        input()
        exit()


def executesqlurls():
    argdis = False
    try:
        connection=apsw.Connection(args.urls)
    except:
        exit()
    cursor=connection.cursor()
    try:
        for row in cursor.execute("SELECT * FROM urls_table"):
            tUrl = row[0]
            nUrl = urllib.parse.unquote(tUrl)
            url.append(nUrl)
            timeMentioned.append(row[1])
            lastMentioned.append(row[2])
            mentionedBy.append(row[3])
        try:
            if args.output is None:
                f = open("urlsreport.csv", 'w')
            else:
                f = open(args.output, 'w')
                argdis = True
            with f:
                fnames = ['url', 'time_mentioned', 'last_mentioned', 'mentioned_by']
                writer = csv.writer(f)
                writer = csv.DictWriter(f, fieldnames=fnames)
                writer.writeheader()
                maxNum = len(url)
                counter = 0 
                while counter < maxNum:
                    writer.writerow({'url':url[counter],'time_mentioned':timeMentioned[counter],
                    'last_mentioned':lastMentioned[counter], 'mentioned_by':mentionedBy[counter]})
                    counter = counter + 1
            f.close()
            if argdis == True:
                print('\x1b[6;30;42m' + 'Exported TS3 Urls data to ' + args.output + '\x1b[0m')
            else:
                print('\x1b[6;30;42m' + 'Exported TS3 Urls data to ' + 'urlsreport.csv' + '\x1b[0m')
        except:
            print('\x1b[1;31m'+'ERROR! Unable to open' + args.output + 'are you specifying the correct path?' + '\x1b[0m')
            print('\x1b[1;31m'+'Be sure to specify the ABSOLUTE path. You can use PWD on linux to find the Absolute Path' + '\x1b[0m')
            print('\x1b[1;31m'+'Here\'s an example of a pathway searchcli.py -f file.localstorage -o /home/ubuntu/workspace/test/file.csv'+ '\x1b[0m')
            print('Press ENTER to terminate the application.')
            input()
            exit()
    except:
        print('\x1b[1;31m'+'ERROR! Unable to open SQL file '+ args.urls +'are you specifying the correct http_discordapp.com_0.localstorage file?' + '\x1b[0m')
        print('Press ENTER to terminate the application.')
        input()
        exit()

            
if args.urls != None:
    executesqlurls()
if args.settings != None:
    executesqlsettings()