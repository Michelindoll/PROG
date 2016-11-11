import random
import string
import csv
from mail import mail

def id_Generator(size=6, chars=string.ascii_uppercase + string.digits):
    """Er wordt een code gemaakt door een string van ascii characters en een string van cijfers te importen deze wordt in een random volgorde aan alkaar geplakt.
    Er wordt niet gecontroleerd of het ID uniek is omdat de kans op twee dezelfde ID's nihiel is"""
    return ''.join(random.choice(chars) for _ in range(size))

def registreren():
    """ Gebruikers input wordt genomen en wordt geschreven in het gebruikers csv file"""
    while True:
        print('Om te registreren hebben wij enkele persoonlijke gegevens nodig.')
        naam = input('Uw voor en achternaam: ')
        email = input('Uw email-adres: ')
        modelFiets = input('Het model van uw fiets: ')
        print('Registratie gelukt!\n')
        schrijfFile(id_Generator(),naam, email, modelFiets)
        break


def schrijfFile(ID, naam, email, fietsModel):
    """verwijst naar de mail functie"""
    with open('gebruikers.csv', 'a', newline='') as gebruikersGegevens:
        writer = csv.writer(gebruikersGegevens)
        writer.writerow((ID, naam, email, fietsModel))
    mail(ID, naam, email, fietsModel)


