import datetime
import time
import calendar

MM, DD = input('Enter you bday in MM DD format: ').split()

#etoday=int(time.time())
#ebday=-9999999999
mm=int(time.strftime('%m'))
dd=int(time.strftime('%d'))
yy=int(time.strftime('%Y'))
MM=int(MM)
DD=int(DD)
counter=0
print(mm, dd, yy, MM, DD)

#yy=int(time.strftime('%Y')
#bday_string = str(MM)+" "+str(DD)+" "+str(YYYY)
#print(yy)
#if MM == 2 and DD == 29:
#    print("Leap year baby!!!!!")
if MM > mm or MM == mm and DD > dd:
    yy=yy-1
else:
    print("do nothing")

while counter < 10:
    if MM == 2 and DD == 29 and not calendar.isleap(yy):
        yy=yy-1
        continue
    else:
        bday_string = str(MM)+" "+str(DD)+" "+str(yy)
        bday_date = datetime.datetime.strptime(bday_string, '%m %d %Y').strftime('%B %d %Y was a %A')
        print(bday_date)
        counter=counter+1
        yy=yy-1
#    bday_date = datetime.datetime.strptime(bday_string, '%m %d %Y')
#    fbday_date=bday_date.strftime('%B %d %Y was a %A')
#    print(fbday_date)
#    YYYY=int(YYYY)+1
#    ebday=int(bday_date.strftime('%s'))


#byr = datetime.datetime.strptime(bday, ' %m %d %Y')
#days = [ 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
#print(days[bday])
#print(byr)
