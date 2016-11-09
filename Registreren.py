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

        gebruikersGegevens = open('tempgebruikers.csv', 'w')
        nameInput = input('Voer uw voor en achternaam in: ')
        emailInput = input('Voer uw Email in: ')
        bankPinNummerinput = input('PIN: ')
        fietsModelInput = input('Voer uw fiets model in: ')
        gebruikersGegevens.write(nameInput + '\n')
        gebruikersGegevens.write(emailInput + '\n')
        gebruikersGegevens.write(bankPinNummerinput + '\n')
        gebruikersGegevens.write(fietsModelInput + '\n')
        gebruikersGegevens.write(id_Generator())
        break




registreren()

