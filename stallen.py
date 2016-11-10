import time
import csv
def nummerCheck():
    #pakt het ingevoerde nummer van de gebruiker
    ingevoerdeNummer = (input('Voer uw gebruikersnummer in. '))
    #kijkt of het nummer bestaat in gebruikers.csv
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dictList = []
    for line in reader:
        dictList.append(line)
    for dict in dictList:
        if ingevoerdeNummer in dict['id']:
            return('Uw ID ' + ingevoerdeNummer + ' is geaccepteerd.')
        else:
            return('Uw ID ' + ingevoerdeNummer + ' is niet correct. Controleer uw ID in uw e-mail.')
def naamCheck():
    #pakt de ingevoerde naam van de gebruiker
    ingevoerdeNaam = input("Voer uw voor en achternaam in. ")
    "Kijkt of de naam bestaat in gebruikers.csv"
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if ingevoerdeNaam in dict['naam']:
            return('Uw naam ' + ingevoerdeNaam + ' is geaccepteerd.')
        else:
            return('Uw naam ' + ingevoerdeNaam + ' is niet correct. Controleer uw naam in uw e-mail.')
def datumEnTijd():
    #geeft huidige datum en tijd
    tijdStip = int(time.time())
    return tijdStip
def schrijftNaarGestaldeFietsen(ingevoerdeNummer, ingevoerdeNaam, tijdStip):
    with open('fietsen.csv', 'a') as fietsFile:
        writer = csv.writer(fietsFile)
        writer.writerow(int((ingevoerdeNummer), int(tijdStip), ingevoerdeNaam))
schrijftNaarGestaldeFietsen(nummerCheck(), datumEnTijd(), str(naamCheck()))

# Code van Les 7
def schrijfFile(kluisnummer,code):
    with open('kluizen.csv', 'a', newline='') as kluisFile:
        writer = csv.writer(kluisFile)
        writer.writerow((kluisnummer, int(code)))
