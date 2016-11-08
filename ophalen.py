import time
import datetime

def naamInvoeren():
    #pakt de ingevoerde naam van de gebruiker
    ingevoerdeNaam = input("Voer uw voor en achternaam in. ")
    return ingevoerdeNaam

def nummerCheck(nummer):
    "kijkt of het nummer bestaat in fietsen.csv"
    reader = csv.DictReader(open('fietsen.csv', 'r'))
    dict_list = []
    for line in reader:

# check of de fiets bij de gebruiker  hoort
