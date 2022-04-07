#!/usr/bin/python3

import datetime
import time
import calendar

MM, DD = input('Enter you bday in MM DD format: ').split()

#set variables to int
mm=int(time.strftime('%m'))
dd=int(time.strftime('%d'))
yy=int(time.strftime('%Y'))
MM=int(MM)
DD=int(DD)
counter=0

#account for upcoming birthdays in year
if MM > mm or MM == mm and DD > dd:
    yy=yy-1

while counter < 10:
    #continue while if not leap yr. Decrement year
    if MM == 2 and DD == 29 and not calendar.isleap(yy):
        yy=yy-1
        continue
    else:
    #print date and day of week. Decrement year. Increment counter    
        bday_string = str(MM)+" "+str(DD)+" "+str(yy)
        bday_date = datetime.datetime.strptime(bday_string, '%m %d %Y').strftime('%B %d %Y was a %A')
        print(bday_date)
        counter=counter+1
        yy=yy-1
