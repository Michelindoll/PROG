import csv

def aantalPlaatsenBeschikbaar():
    with open('fietsen.csv', 'r') as csvfile:
        fietsen = csvfile.readlines()
        output = 501 - len(fietsen)
        if output <= 0:
            return 'Er zijn geen plaatsen beschikbaar'
        else:
            return 'Er zijn '+str(output)+' plaatsen beschikbaar'

def modelFiets(naam):
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if naam in dict['naam']:
            print('Gebruiker ' + dict['naam']+' heeft een '+dict['model'])

modelFiets('Donald Trump')

print(aantalPlaatsenBeschikbaar())
