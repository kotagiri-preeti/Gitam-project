import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
fromaddr = "kpreethi197@gmail.com"
toaddr = "kpreethi197@gmail.com"
msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Subject of the Mail"
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain')) 
filename = "abc.txt"
attachment = open("f:/abc.txt", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls() 
s.login("kpreethi197@gmail.com", "preethi19793") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit()

