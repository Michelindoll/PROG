import smtplib

def mail(naar):

    #Naar en van wie je de email stuurt.
    to = naar
    live_user = 'schoolhu2016@hotmail.com'
    live_pwd = 'ProjectTeam2'

    #Instellingen voor de verzendende email.
    smtpserver = smtplib.SMTP("smtp.live.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(live_user, live_pwd)

    #Zet de gegevens op de juiste plaats. De tekst die hij uiteindelijk mee verstuurd.
    header = 'To:' + to + '\n' + 'From: ' + live_user + '\n' + 'Subject:Test \n'
    print(header)
    msg = header + '\nDit is een test bericht van Project team 2! \n\n'

    #verstuurd de mail en als het lukt, print done! uit. Het sluit daarna de server af.
    smtpserver.sendmail(live_user, to, msg)
    print('done!')
    smtpserver.quit()

#Vraagt naar de nodige gegevens en stuurd vervolgens de standaard email.
print('Typ hier naar wie de Email moet gaan.\n')
mail(input('To: '))
