import time
import datetime
def nummerInvoeren():
    #pakt het ingevoerde nummer van de gebruiker
    ingevoerdeNummer = int(input("Voer uw gebruikersnummer in. "))
    return ingevoerdeNummer
def nummerCheck(nummer):
    "kijkt of het nummer bestaat in gebruikers.csv"
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if nummer in dict['id']:
            print('Uw ID ' + dict['id'] + ' is geaccepteerd.')
        else:
            print('Uw ID ' + dict['id'] + ' is niet correct. Controleer uw ID in uw e-mail.')
def naamInvoeren():
    #pakt de ingevoerde naam van de gebruiker
    ingevoerdeNaam = input("Voer uw voor en achternaam in. ")
    return ingevoerdeNaam
def naamCheck(naam):
    "Kijkt of de naam bestaat in gebruikers.csv"
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if naam in dict['naam']:
            print('Uw naam ' + dict['id'] + ' is geaccepteerd.')
        else:
            print('Uw naam ' + dict['id'] + ' is niet correct. Controleer uw naam in uw e-mail.')
def datumEnTijd():
    #geeft huidige datum en tijd
    huidigeDatumEnTijd = datetime.datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
    return huidigeDatumEnTijd
nummerInvoeren()
nummerCheck(nummerInvoeren())
naamInvoeren()
naamCheck(naamInvoeren())
