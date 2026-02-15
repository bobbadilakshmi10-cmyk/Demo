'''name=input("enter the name")
for i in name:
    print(i,"_",ord(i))'''

#calendar module
'''import calendar
year=2026
month=3
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
year=int(input("enter the year:"))
month=int(input("enter the month:"))
print(calendar.month(year,month))'''

#date
'''from datetime import date
a=date.today()
print(a)

import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time()
'''import time
a=time.time()
print(a)

b=time.localtime()
print(b)

print(f"today date is{b.tm_mday}-{b.tm_mon}-{b.tm_year}")

#tm_hour=10, tm_min=10, tm_sec=10,

print(f"time is{b.tm_hour}-{b.tm_min}-{b.tm_sec}")

print(f"day is{b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

import random
import time
for i in range(10):
    n=random.randint(1000,9999)
    print(n)
    time.sleep(1)


