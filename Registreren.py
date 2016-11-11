import random
import string
import csv

def id_Generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def registreren():

    while True:
        print('Welkom Bij Goat Sec fiets stallingen!')
        print('Om te registreren bij Goat Sec hebben wij enkele persoonlijke gegevens nodig.')
        print('Uw persoonlijke gegevens worden natuurlijk veilig opgeslagen.')
        print('Uw persoonlijke gegevens worden natuurlijk niet misbruikt door Goat Sec Inc.')
        naam = input('Uw voor en achternaam: ')
        email = input('Uw email-adres: ')
        modelFiets = input('Het model van uw fiets: ')
        print('Registratie gelukt!')
        schrijfFile(id_Generator(),naam, email, modelFiets)
        break


def schrijfFile(ID, naam, email, fietsModel):
    with open('gebruikers.csv', 'a', newline='') as gebruikersGegevens:
        writer = csv.writer(gebruikersGegevens)
        writer.writerow((ID, naam, email, fietsModel))
    mail = open('mail.py', 'r')
    mail.mail()


