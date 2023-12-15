import smtplib

smtpobj=smtplib.SMTP('smtp.gmail.com',587) 
smtpobj.ehlo
smtpobj.starttls()

smtpobj.login('ullaspatel713@gmail.com','UllasPatel@69')

smtpobj.sendmail("ullaspatel713@gmail.com","ritviksshetty@gmail.com",'Subject: SMTP Check. \n This is a test email')
smtpobj.quit()



