import smtplib

def mail(naar, van, wachtwoord):

    #Naar en van wie je de email stuurt.
    to = naar
    live_user = van
    live_pwd = wachtwoord

    #Instellingen voor de verzendende email.
    smtpserver = smtplib.SMTP("smtp.live.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(live_user, live_pwd)

    #Zet de gegevens op de juiste plaats. De tekst die hij uiteindelijk mee verstuurd.
    header = 'To:' + to + '\n' + 'From: ' + live_user + '\n' + 'Subject:Test \n'
    print (header)
    msg = header + '\n Dit is een test bericht! \n\n'

    #verstuurd de mail en als het lukt, print done! uit. Het sluit daarna de server af.
    smtpserver.sendmail(live_user, to, msg)
    print ('done!')
    smtpserver.quit()

#Vraagt naar de nodige gegevens en stuurd vervolgens de standaard email.
print('Email naar, Email van u(moet een live/hotmail zijn), Uw email wachtwoord')
mail(input(), input(), input())