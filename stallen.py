import time
import csv

def nummerCheck():
    #pakt het ingevoerde nummer van de gebruiker
    global ingevoerdeNummer
    ingevoerdeNummer = (input('Voer uw gebruikersnummer in. '))
    global counter
    counter = 0
    #kijkt of het nummer bestaat in gebruikers.csv
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dictList = []
    for line in reader:
        dictList.append(line)
    for dict in dictList:
        if ingevoerdeNummer in dict['id']:
            counter +=1
            return('Uw ID ' + ingevoerdeNummer + ' is geaccepteerd.')
        else:
            return('Uw ID ' + ingevoerdeNummer + ' is niet correct. Controleer uw ID in uw e-mail.')
def naamCheck():
    #pakt de ingevoerde naam van de gebruiker
    global ingevoerdeNaam
    ingevoerdeNaam = input("Voer uw voor en achternaam in. ")
    "Kijkt of de naam bestaat in gebruikers.csv"
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if ingevoerdeNaam in dict['naam']:
            counter +=1
            return('Uw naam ' + ingevoerdeNaam + ' is geaccepteerd.')
        else:
            return('Uw naam ' + ingevoerdeNaam + ' is niet correct. Controleer uw naam in uw e-mail.')
def datumEnTijd():
    #geeft huidige datum en tijd
    huidigeDatumEnTijd = time.time()
    return huidigeDatumEnTijd

def schrijfFile(nummer, datum, naam):
    with open('fietsen.csv', 'a', newline='') as fietsFile:
        writer = csv.writer(fietsFile)
        writer.writerow((nummer, datum, naam))

schrijfFile('0003','12345678','Michel Wijkstra')
