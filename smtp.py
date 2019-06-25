import smtplib
sender = 'preethi.kotagiri@gmail.com'
receivers = 'preethi.kotagiri@gmail.com'
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
except:
    print("Error: unable to send email")