#updated!
import requests

content = requests.get('https://raw.githubusercontent.com/ccpandhare/nalandalite/pygitfetch/filetoupdatefrom.py').text

file = open('index.py','rw')

gotname = False
j = -1

while gotname == False:
    j = j+1
    try:
        getBackup = open('backups/index.backup'+ str(j) +'.py','r')
    except IOError:
        gotname = True

if file.read() != content:
    print "\n\tUpdate Available!"
    backupFile = open('backups/index.backup'+ str(j) +'.py','w+')
    backupFile.write(file.read())
    print "\n\tbackup written in : backups/index.backup" + str(j) +'.py'
    print open('index.py','w').write(content)
    print "index.py updated"
else:
    print "File is up-to-date!"
