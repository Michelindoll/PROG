# In dit bestand komt enkel de interface, geen functies in plakken
from info import aantalPlaatsenBeschikbaar, modelFiets
from beheerderspaneel import inloggenBeheer
from Registreren import registreren
from stallen import nummerNaamCheck
from ophalen import fietsOphalen

def showInterface():
    """Begint de interface loop, vanuit hier worden alle andere functie calls uitgevoerd."""
    while True:
        print('Welkom bij de NS Fietsenstalling')
        print('Kies 1 om te registreren')
        print('Kies 2 om uw fiets te stallen')
        print('Kies 3 om uw fiets op te halen')
        print('Kies 4 om informatie op te vragen')
        invoer = int(input('Maak uw keuze: '))
        if invoer == 0:
            print('')
            inloggenBeheer()
        if invoer == 1:
            print('')
            registreren()
        if invoer == 2:
            print('')
            nummerNaamCheck()
        if invoer == 3:
            print('')
            fietsOphalen()
        if invoer == 4:
            print('')
            print('Menu voor het opvragen van informatie:')
            print('Kies 1 voor algemene informatie:')
            print('Kies 2 voor persoonlijke informatie')
            invoer = int(input('Maak uw keuze: '))
            if invoer == 1:
                print('')
                print('Menu voor het opvragen van algemene informatie:')
                print('Kies 1 voor het aantal beschikbare plaatsen')
                print('Kies 2 voor onze voorwaarden')
                invoer = int(input('Maak uw keuze: '))
                if invoer == 1:
                    print('')
                    print(aantalPlaatsenBeschikbaar())
                    print('')
                if invoer == 2:
                    print('')
                    print('Fiets weg? - Eigen schuld')
                    print('Band lek? - Eigen schuld')
                    print('Fietsenstalling afgebrand? - Eigen schuld')
                    print('thermonucleaire oorlog uitgebroken? - Eigen schuld')
                    print('')
                    del invoer #Zorgt dat er niet naar het blok hieronder gesprongen wordt.
            if invoer == 2:
                print('')
                print('Voer uw naam in om uw persoonlijke gegevens op te vragen.')
                invoer = input('Naam: ')
                modelFiets(invoer)
                print('')

showInterface()


