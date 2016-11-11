import csv

def fietsOphalen():
    "kijkt of het nummer bestaat in fietsen.csv"
    nummer = input('Voer uw ID in: ')
    naam = input('Voer uw voor en achternaam in: ')
    reader = csv.DictReader(open('fietsen.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if nummer in dict['id'] and naam in dict['naam']:
            verwijderFiets(nummer)
            print('Fiets vrijgegeven!')

# check of de fiets bij de gebruiker hoort
# print ga fietsen en vervolgens verwijderen uit gestaalde fiets csv.


def verwijderFiets(id):
    """Leest fietsen.csv, zoekt de regel waar het ID overeenkomt met het variabel id (string) en verwijderd deze. Daarna wordt de het CSV bestand weer opgeslagen."""
    with open('fietsen.csv', 'r') as csvfile:
        fietsen = csvfile.readlines()
        for row in fietsen:
            if id in row:
                fietsen.remove(row)
    with open('fietsen.csv', 'w') as csvfile:
        csvfile.writelines(fietsen)

