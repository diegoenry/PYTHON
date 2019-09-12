# ORIGINAL from here:
# https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
  
## ADDED by dgomes
import getpass

email_from = input("Sender e-mail: ")
password = getpass.getpass("Password: ")

email_to = ['diego.enry@gmail.com','diego@biof.ufrj.br']

## END ADDED by dgomes


fromaddr = email_from # !by dgomes
toaddr = email_to     # !by dgomes
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
# !by dgomes  #msg['To'] = toaddr
msg['To'] = ', '.join(toaddr)
  
# storing the subject  
msg['Subject'] = "[ENMC] Test attachment, multiplos destinos"
  
# string to store the body of the mail 
body = "Please get the attached PDF file"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "ACEITE_ENMC_ECTM_2019_ID_326.pdf"
attachment = open("/home/dgomes/Downloads/certificados_enmc2019/ACEITES_BK/ACEITE_ENMC_ECTM_2019_ID_326.pdf", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.ufjf.edu.br', 587) # ! by dgomes 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, password) 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 
