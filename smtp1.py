import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.ehlo()
s.starttls()
message='''hello everyone
this is preeti
saying good morning'''
s.login("kpreethi197@gmail.com","preethi19793")
s.sendmail("kpreethi197@gmail.com","kpreethi197@gmail.com","subject: this is subject \n\n %s "%message)
s.quit()
