import csv
import os
from datetime import date
from datetime import datetime

attr={}
def get_oncall():
  global attr
  f = open( 'timetable.csv', 'rU' ) #open the file in read universal mode
  p = open( 'picture_mapping.csv', 'r')
  picture_path = {}
  for line in p:
    name,path=line.split(',')
    picture_path[name]=path
  for line in f:
    cell = line.split( "," )
    date_object =  datetime.strptime(cells[0], '%m/%d/%Y')
    if datetime.combine(date_object,datetime.min.time()) == datetime.combine(date.today(), datetime.min.time()):
      attr['date'] = cell[0]
      atrr['user1'] = [cell[1],picture_path[cell[1]]
      attr['user2'] = [cell[2],picture_path[cell[2]]

  return attr
