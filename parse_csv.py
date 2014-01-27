import csv
import os
from datetime import date
from datetime import datetime
file_path = os.path.abspath('/home/pi/ut_repo/oncall_ut/timetable.csv')
f = open( file_path, 'rU' ) #open the file in read universal mode
for line in f:
       cells = line.split( "," )
       date_object =  datetime.strptime(cells[0], '%m/%d/%Y')
       if datetime.combine(date_object,datetime.min.time()) == datetime.combine(date.today(), datetime.min.time()):
            print cells[ 0 ] #since we want the first, second and third column 

