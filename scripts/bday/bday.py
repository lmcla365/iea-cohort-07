#!/usr/bin/python3

import datetime
import time
import calendar

MM, DD = input('Enter your bday in MM DD format: ').split()

#test for digit input
if not MM.isdigit() or not DD.isdigit():
    print("Invalid input")
    exit()

#set variables to int
mm=int(time.strftime('%m'))
dd=int(time.strftime('%d'))
yy=int(time.strftime('%Y'))
MM=int(MM)
DD=int(DD)
counter=0

if (MM > 12 or MM < 1) or (DD < 1 or DD > 31) or (MM == 4 or MM == 6 or MM == 9 or MM == 11 and DD > 30) or (MM == 4 and DD > 29):
    print("Invalid input")
    exit()

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
