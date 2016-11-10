import csv

def aantalPlaatsenBeschikbaar():
    """Deze functie leest het fietsen bestand, door het aantal regels van 501 af te trekken berekend het de beschikbare plaatsen."""
    with open('fietsen.csv', 'r') as csvfile:
        fietsen = csvfile.readlines()
        output = 501 - len(fietsen)
        if output <= 0:
            return 'Er zijn geen plaatsen beschikbaar'
        else:
            return 'Er zijn '+str(output)+' plaatsen beschikbaar'

def modelFiets(naam):
    """Deze functie maakt per gebruiker een dictionary en vergelijkt het naam veld met de invoer. Als er een overeenkomst is wordt de regel afgedrukt."""
    #Todo: Error handling bij meer dan 1 gebruiker met dezelfde naam
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    dict_list2 = []
    counter = 0
    for line in reader:
        dict_list.append(line)
    for dict in dict_list:
        if naam in dict['naam']:
            #print('Gebruiker ' + dict['naam']+' heeft een '+dict['model'])
            counter +=1
            dict_list2.append(dict)
    if counter == 0:
        print('Gebruiker niet gevonden!')
    if counter == 1:
        for dict in dict_list2:
            print('Gebruiker ' + dict['naam']+' heeft een '+dict['model'])
    if counter > 1:
        print('Er zijn meerde gebruikers gevonden met de naam '+naam)

modelFiets('Donald Trump')





