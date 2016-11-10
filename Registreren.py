import random
import string
import csv

def id_Generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(id_Generator())

def registreren():

    while True:
        print('Welkom Bij Goat Sec fiets stallingen!')
        print('Om te registreren bij Goat Sec hebben wij enkele persoonlijke gegevens nodig.')
        print('Uw persoonlijke gegevens worden natuurlijk veilig opgeslagen.')
        print('Uw persoonlijke gegevens worden natuurlijk niet misbruikt door Goat Sec Inc.')
        schrijfFile()
        break


def schrijfFile(ID, naam, email, fietsModel):
    with open('gebruikers.csv', 'a', newline='') as gebruikersGegevens:
        writer = csv.writer(gebruikersGegevens)
        writer.writerow((ID, naam, email, fietsModel))
        ID = id_Generator()
        naam = input('Voer uw voor en achternaam in: ')
        email = input('Voer uw Email in: ')
        fietsModel = input('Voer uw fiets model in: ')




registreren()

