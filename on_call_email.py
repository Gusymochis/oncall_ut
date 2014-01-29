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

addr_book = {}
def lookup_addr():
  global addr_book
  print file_path
  f = open( file_path, 'rU' ) #open the file in read universal mode
  for line in f:
    print line
    #name,email = line.split(',')
    data = line.split(',')
    name = data[0]
    email = data[1] 
    addr_book[name]=email
  f.close()


def send_email(name):
    global addr_book
    if not name:
        print 'name is required'
        return;
    #email body
    msg = MIMEText('get ready')

    #put your from and to address here
    msg['Subject'] = 'You are on call'
    msg['From'] = fromaddr
    toaddr = addr_book[name] 
    msg['To'] = toaddr 

    s = smtplib.SMTP(smtp_server)
    print "send email to %s" % toaddr
    s.sendmail(fromaddr, [toaddr], msg.as_string())
    s.quit()


