import smtplib
from email.mime.text import MIMEText

#email body
msg = MIMEText('get ready')

#put your from and to address here
fromaddr = ''
toaddr = ''
msg['Subject'] = 'You are on call'
msg['From'] = fromaddr 
msg['To'] = toaddr

#put your smtp server here
smtp_server = ''
s = smtplib.SMTP(smtp_server)
s.sendmail(fromaddr, [toaddr], msg.as_string())
s.quit
