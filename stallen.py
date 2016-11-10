import time
import csv
def nummerNaamCheck():
    #pakt het ingevoerde nummer van de gebruiker
    global ingevoerdeNummer
    ingevoerdeNummer = (input('Voer uw ID in. '))
    global ingevoerdeNaam
    ingevoerdeNaam = input("Voer uw voor en achternaam in. ")
    #kijkt of het nummer bestaat in gebruikers.csv
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dictList = []
    for line in reader:
        dictList.append(line)
    for dict in dictList:
        if ingevoerdeNummer in dict['id'] and ingevoerdeNaam in dict['naam']:
            global counter
            counter +=1
            print('Uw ID ' + ingevoerdeNummer + ' en uw naam ' + ingevoerdeNaam + ' is geaccepteerd.')
        if counter == 1:
            schrijfFile(ingevoerdeNummer, datumEnTijd(), ingevoerdeNaam)
            break
    if counter != 1:
        print('Uw ID of uw Naam is niet correct.')
        nummerNaamCheck()
def datumEnTijd():
    #geeft huidige datum en tijd
    huidigeDatumEnTijd = int(time.time())
    return huidigeDatumEnTijd
def schrijfFile(nummer, datum, naam):
    with open('fietsen.csv', 'a', newline='') as fietsFile:
        global counter
        if counter == 1:
            writer = csv.writer(fietsFile)
            writer.writerow((nummer, datum, naam))
counter = 0
nummerNaamCheck()
