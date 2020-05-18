#DateTime Module video 91
import datetime

#Creating a time stamp h:m:S
time = datetime.time(5,25,1)
print(time)
print(time.hour)


#Finding the min / max value of time
print(datetime.time.min)
print(datetime.time.max)

#Creating a date Y-M-D
date = datetime.date.today()
print(date)

#Amending existing dates
date1 = datetime.date(2015,3,11)
date2 = date1.replace(year=2020)
print(date2)

#Checking for date / time differences

daysdifference = (date2 - date1)
fprint(daysdifference)
