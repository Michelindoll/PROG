import smtplib

def mail(naar, van, wachtwoord):

    #Naar en van wie je de email stuurt
    to = naar
    live_user = van
    live_pwd = wachtwoord

    #instellingen voor de verzendende email
    smtpserver = smtplib.SMTP("smtp.live.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(live_user, live_pwd)

    header = 'To:' + to + '\n' + 'From: ' + live_user + '\n' + 'Subject:testing \n'
    print (header)
    msg = header + '\n this is test msg from Davey Groen \n\n'

    smtpserver.sendmail(live_user, to, msg)
    print ('done!')
    smtpserver.quit()

print('Email naar, Email van u, Uw email wachtwoord')
mail(input(), input(), input())
