props = {}
props['email_addr_filename']="email_addr.csv"
props['smtp_server']="mail.server.com"
props['from_addr']="pi_ut@server.com"

if len(props) == 0:
  print 'WARNING: Define properties in properties.py'
