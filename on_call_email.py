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
#def lookup_addr(name):
def lookup_addr():
  global addr_book
  f = open( file_path, 'rU' ) #open the file in read universal mode
  for line in f:
    cells = line.split( "," )
    #if (cells[0] == name):
    #  return cells[1]
    addr_book={cells[0]:cells[1]}
  f.close()


#def send_email(toaddr):
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
    s.sendmail(fromaddr, [toaddr], msg.as_string())
    s.quit

#def lookup_and_send(name):
    #toaddr = lookup_addr(name)
    #print "found address " + addr_book[name] 
    #send_email(toaddr)
    #print "sent email"

