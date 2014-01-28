import csv
import os
import datetime
#import espeak
from datetime import date
from datetime import datetime
from datetime import timedelta
file_path = os.path.relpath('./timetable.csv')

def compute_monday():
	today = date.today()
        offset = (today.weekday() - 0) % 7
	last_monday = today - timedelta(days=offset)
        convertedDate =	datetime.combine(last_monday, datetime.min.time())
	return convertedDate

def get_oncall():
 f = open( file_path, 'rU' ) #open the file in read universal mode
 for line in f:
    cells = line.split( "," )
    dt =  datetime.strptime(cells[0], '%m/%d/%Y')
    month,day,year = (int(x) for x in cells[0].split('/'))
    oldDate = date(year,month,day)
    dayofWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date_object =  datetime.strptime(cells[0], '%m/%d/%Y')
   
    if datetime.combine(date_object,datetime.min.time()) == compute_monday():
        #os.system('espeak "on call" + cells[ 0 ] + " " + cells[1] + " " + cells[2]')
        return cells[ 0 ] + " " + cells[1] + " " + cells[2] #since we want the first, second and third column


 
  
