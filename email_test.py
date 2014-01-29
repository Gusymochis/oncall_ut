import on_call_email
import parse_csv

attrib = parse_csv.get_oncall();

name1 = attrib['user1'][0]
name2 = attrib['user2'][0]
on_call_email.lookup_addr()
on_call_email.send_email(name1)
on_call_email.send_email(name2)

