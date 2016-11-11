#importeert csv
import csv

def inloggenBeheer():

    # zorgt ervoor dat je in moet loggen om bij het beheerderspaneel te komen via gebruikersnaam en wachtwoord
    username = 'admin'
    password = 'nstrein'
    while True:
            print('Om in te loggen dient u een medewerker te zijn!')
            invoerusername = input('username: ')
            invoerpassword = input('password: ')

            # correcte invoer opent het beheerdersPaneel
            if invoerusername == username and invoerpassword == password:
                print("")
                print('correct')
                print("")
                beheerdersPaneel()

            # incorrecte invoer opent opnieuw het inloggenBeheer
            else:
                print("")
                print('incorrect username or password')
                print("")
                inloggenBeheer()


def beheerdersPaneel():
    # in het beheerderspaneel kan je de gebruikers gegevens inlezen.
    while True:
            print('Welkom bij het beheerderspaneel')
            print('Kies 1 om alle gegevens in te zien')
            print('Kies 2 om terug naar het hoofdmenu te gaan')
            invoer = int(input('Maak uw keuze: '))

            # bij het invoeren van keuze 1 importeert en leest hij gebruikers.csv
            if invoer == 1:
                print("")
                print('lees csv bestand')
                print("")
                with open('gebruikers.csv') as csvfile:
                    gebruikersgegevens = csv.reader(csvfile)
                    for row in gebruikersgegevens:
                        print(''.join(row))
                    print('')
                    beheerdersPaneel()

            # bij het invoeren van 2 ga je weer terug naar het hoofdmenu
            if invoer == 2:
                print('u bent terug bij het hoofdmenu')
                import main.py

            # geeft een melding dat je alleen uit keuze 1 en 2 kan kiezen. en stuurt je dan weer terug naar het beheerderspaneel
            if invoer != 1 and 2:
                print('kies uit optie 1 of 2')
                beheerdersPaneel()
            return


inloggenBeheer()
