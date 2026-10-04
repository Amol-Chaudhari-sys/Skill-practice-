import smtplib

to = input ("enter the receivers Email ")
message = input ("Enter the message ")
def email_auto (to , message ):
    server = smtplib.SMTP('smtp.gmail.com', 587 )
    server.starttls()
    server.login("sender e mail ", 'password ')
    server.sendmail("sender mail", to , message )
    server.close()
email_auto(to , message )