import time
import csv
def nummerCheck():
    #pakt het ingevoerde nummer van de gebruiker
    global ingevoerdeNummer
    ingevoerdeNummer = (input('Voer uw ID in. '))
    #kijkt of het nummer bestaat in gebruikers.csv
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dictList = []
    for line in reader:
        dictList.append(line)
    for dict in dictList:
        if ingevoerdeNummer not in dict['id']:
            print('Uw ID ' + ingevoerdeNummer + ' is niet correct. Controleer uw ID in uw e-mail.')
            nummerCheck()
        if ingevoerdeNummer in dict['id']:
            global counter
            counter +=1
            print('Uw ID ' + ingevoerdeNummer + ' is geaccepteerd.')
            naamCheck()
            break
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
        if ingevoerdeNaam not in dict['naam']:
            print('Uw naam ' + ingevoerdeNaam + ' is niet correct. Controleer uw naam in uw e-mail.')
            naamCheck()
        if ingevoerdeNaam in dict['naam']:
            global counter
            counter +=1
            print('Uw naam ' + ingevoerdeNaam + ' is geaccepteerd.')
            schrijfFile(ingevoerdeNummer, datumEnTijd(),ingevoerdeNaam)
            break
def datumEnTijd():
    #geeft huidige datum en tijd
    huidigeDatumEnTijd = int(time.time())
    return huidigeDatumEnTijd
def schrijfFile(nummer, datum, naam):
    with open('fietsen.csv', 'a', newline='') as fietsFile:
        global counter
        if counter == 2:
            writer = csv.writer(fietsFile)
            writer.writerow((nummer, datum, naam))
        if counter != 2:
            print('Uw ID of uw Naam is incorrect.')
            nummerCheck()

counter = 0
nummerCheck()
