import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.ehlo()
s.starttls()
senderadd="kpreethi197@gmail.com"
message="hello everyone"
s.login(senderadd,"preethi19793")
s.sendmail(senderadd,senderadd,"subject: display subject \n\n %s"%message)
s.quit()
