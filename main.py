# In dit bestand komt enkel de interface, geen functies in plakken
from info import aantalPlaatsenBeschikbaar, modelFiets
from beheerderspaneel import beheerdersPaneel, inloggenBeheer

def showInterface():
    while True:
        print('Welkom bij de NS Fietsenstalling van NS')
        print('Kies 1 om te registreren')
        print('Kies 2 om uw fiets te stallen')
        print('Kies 3 om uw fiets op te halen')
        print('Kies 4 om informatie op te vragen')
        invoer = int(input('Maak uw keuze: '))
        if invoer == :
            print('')
            inloggenBeheer()
        if invoer == 1:
            print('functie call')
        if invoer == 2:
            print('functie call')
        if invoer == 3:
            print('functie call')
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
            if invoer == 2:
                print('')
                print('Voer uw naam in om uw persoonlijke gegevens op te vragen.')
                invoer = input('Naam: ')
                modelFiets(invoer)
                print('')

showInterface()


