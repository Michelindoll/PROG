def inloggenBeheer():
    root = 'alcohol'
    admin = 'bier'
    while True:
            print('Om in te loggen dient u een medewerker te zijn!')
            invoerusername = input('username: ')
            invoerpassword = input('password: ')
            if invoerusername  == admin and invoerpassword == root:
                print('correct')
                beheerdersPaneel()
            else:
                print('incorrect username or password')
                inloggenBeheer()


def beheerdersPaneel():

    while True:
            print('Welkom bij het beheerderspaneel')
            print('Kies 1 om alle gegevens in te zien')
            print('Kies 2 om gegevens te wijzigen')
            invoer = int(input('Maak uw keuze: '))
            if invoer == 1:
                print('lees csv bestand')
                beheerdersPaneel()
            if invoer == 2:
                print('schrijf in csv bestand')
            if invoer != 1 and 2:
                print('kies uit optie 1 of 2')
                beheerdersPaneel()
            return

inloggenBeheer()
