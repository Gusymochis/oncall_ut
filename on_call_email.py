import csv
import os
import smtplib
from email.mime.text import MIMEText
import properties

#put your from and to address here
fromaddr = properties.props['from_addr'] 

#put your smtp server here
smtp_server = properties.props['smtp_server'] 

file_path = os.path.relpath('./'+properties.props['email_addr_filename'])

def lookup_addr(name):
  f = open( file_path, 'rU' ) #open the file in read universal mode
  for line in f:
    cells = line.split( "," )
    if (cells[0] == name):
      return cells[1]

def send_email(toaddr):
    if not toaddr:
        print 'toaddr is required'
        return;
    #email body
    msg = MIMEText('get ready')

    #put your from and to address here
    msg['Subject'] = 'You are on call'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    s = smtplib.SMTP(smtp_server)
    s.sendmail(fromaddr, [toaddr], msg.as_string())
    s.quit

def lookup_and_send(name):
    toaddr = lookup_addr(name)
    print "found address " + toaddr
    send_email(toaddr)
    print "sent email"

