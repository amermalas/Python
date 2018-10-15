#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
delta=timedelta(days=365,hours=5,minutes=1)
print(delta)

# print today's date
today = datetime.now()
print(today)
print("one year from now:"+str(today+delta))

# print today's date one year from now
oneweek= today-timedelta(weeks=1)
print("one week from now it was " + (today-timedelta(weeks=1)).strftime("%A %B %d, %Y"))

# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
today=date.today()
afd = date(today.year,4,1)
if(afd < today):
    print("afd passed by %d days ago"% (today-afd).days)
    afd=afd.replace(year=today.year+1)
time_to_afd=afd-today
print("it is just ",time_to_afd.days,"days until afd")



# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  


