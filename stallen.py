import time
import csv
def nummerNaamCheck():
    """De functie nummerNaamCheck() laat de gebruiker zijn ID en naam invoeren, waarna wordt gekeken
    of deze aanwezig zijn bij de geregistreerde gebruikers."""
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
    """De functie datumEnTijd() genereert een nummer wat gelijk staat aan het aanal seconden sinds
    de epoch."""
    huidigeDatumEnTijd = int(time.time())
    return huidigeDatumEnTijd
def schrijfFile(nummer, datum, naam):
    """De functie schrijfFile opent de file fietsen.csv en kijkt naar de counter. Als deze 1 is,
    wordt er het ID, de Timestamp en de naam opgeslagen. Dit betekend dat er een fiets gestald is."""
    with open('fietsen.csv', 'a', newline='') as fietsFile:
        global counter
        if counter == 1:
            writer = csv.writer(fietsFile)
            writer.writerow((nummer, datum, naam))
counter = 0
