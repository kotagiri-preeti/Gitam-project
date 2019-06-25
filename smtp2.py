import smtplib 
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]
for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.ehlo()
    s.starttls() 
    s.login("sender_email_id", "sender_email_id_password") 
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", li[i], message) 
    s.quit() 
