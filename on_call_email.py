import smtplib
from email.mime.text import MIMEText

msg = MIMEText('get ready') 
fromaddr = ''
toaddr = ''
msg['Subject'] = 'You are on call'
msg['From'] = fromaddr 
msg['To'] = toaddr

s = smtplib.SMTP('')
s.sendmail(fromaddr, [toaddr], msg.as_string())
s.quit
