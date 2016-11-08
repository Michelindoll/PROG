import time
import datetime

def nummerInvoeren():
    #pakt het ingevoerde nummer van de gebruiker
    ingevoerdeNummer = int(input("Voer uw gebruikersnummer in. "))
    return ingevoerdeNummer

def naamInvoeren():
    #pakt de ingevoerde naam van de gebruiker
    ingevoerdeNaam = input("Voer uw voor en achternaam in. ")
    return ingevoerdeNaam

def datumEnTijd():
    #geeft huidige datum en tijd
    huidigeDatumEnTijd = datetime.datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
    return huidigeDatumEnTijd

