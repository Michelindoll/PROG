import smtplib
import csv

def mail(ID, naam, email, modelFiets):

    #Opent het bestand gebruikers om de benodigde gegevens eruit te halen
    reader = csv.DictReader(open('gebruikers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)

    #Naar en van wie je de email stuurt.
    to = email
    live_user = 'schoolhu2016@hotmail.com'
    live_pwd = 'ProjectTeam2'

    #Instellingen voor de verzendende email.
    smtpserver = smtplib.SMTP("smtp.live.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(live_user, live_pwd)

    #Zet de gegevens op de juiste plaats. De tekst die hij uiteindelijk mee verstuurd.
    header = 'To:' + to + '\n' + 'From: ' + live_user + '\n' + 'Subject:Registratie gegevens \n'
    print(header)
    msg = header + '\nHierbij uw gegevens\n\nUw id: ' + str(ID) + '\nUw gebruikersnaam: ' + str(naam) + '\nUw model: ' + str(modelFiets) + '\n\n Met vriendelijke groet,\n ProjectTeam2'

    #verstuurd de mail en als het lukt, print done! uit. Het sluit daarna de server af.
    smtpserver.sendmail(live_user, to, msg)
    print('done!')
    smtpserver.quit()

#Vraagt naar de nodige gegevens en stuurd vervolgens de standaard email.
#print('Typ hier naar wie de Email moet gaan.\n')
#mail(input('To: '))
