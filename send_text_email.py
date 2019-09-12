import smtplib
import getpass

email_from = input("Sender e-mail: ")
password = getpass.getpass("Password: ")

#email_from = 'diego.gomes@ufjf.edu.br'
#password = 'mysecretpassword'

email_to = ['diego.enry@gmail.com','diego@biof.ufrj.br']

# Email
smtp = smtplib.SMTP('smtp.ufjf.edu.br', 587)
smtp.starttls()

smtp.login(email_from, password)
msg = """From: %s
To: %s
Subject: [ENMC] Multi destinatario

Email de teste do Buteco Open Source.""" % (email_from, ', '.join(email_to))

smtp.sendmail(email_from, email_to, msg)

smtp.quit()
