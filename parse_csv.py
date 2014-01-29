import csv
import os
import datetime
#import espeak
from datetime import date
from datetime import datetime
from datetime import timedelta

attr={}

def compute_monday():
  today = date.today()
  offset = (today.weekday() - 0) % 7
  last_monday = today - timedelta(days=offset)
  convertedDate =	datetime.combine(last_monday, datetime.min.time())
  return convertedDate

def get_oncall():
  global attr
  f = open( 'timetable.csv', 'rU' ) #open the file in read universal mode
  p = open( 'pictures.csv', 'r')
  picture_path = {}
  for line in p:
    name,path=line.split('\n')[0].split(',')
    picture_path[name]=path
  for line in f:
    oc_date,name1,name2 = line.split('\n')[0].split(',')
    dt =  datetime.strptime(oc_date, '%m/%d/%Y')
    month,day,year = (int(x) for x in oc_date.split('/'))
    oldDate = date(year,month,day)
    dayofWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date_object =  datetime.strptime(oc_date, '%m/%d/%Y')
   
    if datetime.combine(date_object,datetime.min.time()) == compute_monday():
      attr['date'] = oc_date
      attr['user1'] = [name1,picture_path[name1]]
      attr['user2'] = [name2,picture_path[name2]]

  return attr
 
  
