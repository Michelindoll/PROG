import time
import datetime
import csv

def naamInvoeren():
    #pakt de ingevoerde naam van de gebruiker
    ingevoerdeNaam = input("Voer uw voor en achternaam in. ")
    return ingevoerdeNaam

def nummerCheck(nummer):
    "kijkt of het nummer bestaat in fietsen.csv"
    reader = csv.DictReader(open('fietsen.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if nummer in dict['id']:
            print('ID: ' + dict['id']+' klopt!' )
        else:
            print('ID klopt niet')
# check of de fiets bij de gebruiker hoort

nummerCheck(input('nummer: '))

def verwijderFiets(id):
    """Leest fietsen.csv, zoekt de regel waar het ID overeenkomt met het variabel id (sting) en verwijderd deze. Daarna wordt de het CSV bestand weer opgeslagen."""
    with open('fietsen.csv', 'r') as csvfile:
        fietsen = csvfile.readlines()
        for row in fietsen:
            if id in row:
                fietsen.remove(row)
    with open('fietsen.csv', 'w') as csvfile:
        csvfile.writelines(fietsen)
