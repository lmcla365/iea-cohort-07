import datetime
import time

MM, DD, YYYY = input('Enter you bday in MM DD YYYY format: ').split()
etoday=int(time.time())
ebday=-9999999999

while ebday < etoday:
    bday_string = str(MM)+" "+str(DD)+" "+str(YYYY)
    bday_date = datetime.datetime.strptime(bday_string, '%m %d %Y')
    fbday_date=bday_date.strftime('%B %d %Y was a %A')
    print(fbday_date)
    YYYY=int(YYYY)+1
    ebday=int(bday_date.strftime('%s'))


#byr = datetime.datetime.strptime(bday, ' %m %d %Y')
#days = [ 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
#print(days[bday])
#print(byr)
