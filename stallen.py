import time
import datetime
import csv
def nummerCheck():
    #pakt het ingevoerde nummer van de gebruiker
    ingevoerdeNummer = (input("Voer uw gebruikersnummer in. ")
    #kijkt of het nummer bestaat in gebruikers.csv
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if ingevoerdeNummer in dict['id']:
            print('Uw ID ' + dict['id'] + ' is geaccepteerd.')
        else:
            print('Uw ID ' + dict['id'] + ' is niet correct. Controleer uw ID in uw e-mail.')
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
            print('Uw naam ' + dict['id'] + ' is geaccepteerd.')
        else:
            print('Uw naam ' + dict['id'] + ' is niet correct. Controleer uw naam in uw e-mail.')
def datumEnTijd():
    #geeft huidige datum en tijd
    huidigeDatumEnTijd = datetime.datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
    return huidigeDatumEnTijd
nummerCheck()
naamCheck()
