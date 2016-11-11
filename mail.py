import smtplib


def mail(ID, naam, email, modelFiets):
    """Mailt de code naar de eigenaar van de fiets, de code komt niet op het scherm te staan om veiligheid te garanderen."""
    try:
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
        header = 'To: ' + to + '\n' + 'From: ' + live_user + '\n' + 'Subject: Registratie gegevens \n'
        msg = header + '\nHierbij uw gegevens,\n\nUw id: ' + str(ID) + '\nUw gebruikersnaam: ' + str(naam) + '\nUw model: ' + str(modelFiets) + '\n\n\n Met vriendelijke groet,\n ProjectTeam 2'

        #verstuurd de mail en als het lukt, print done! uit. Het sluit daarna de server af.
        smtpserver.sendmail(live_user, to, msg)
        print('De email is succesvol verstuurd!\n')
        smtpserver.quit()

    except:
        with open('gebruikers.csv', 'r') as csvfile:
            gebruikers = csvfile.readlines()
            for row in gebruikers:
                if ID in row:
                    gebruikers.remove(row)
        with open('gebruikers.csv', 'w') as csvfile:
            csvfile.writelines(gebruikers)

        print('Uw ingevoerde email is onjuist, probeer opnieuw!\n')
