import datetime

today = datetime.datetime.now()
print(today)

todaydate = datetime.date.today()
print(todaydate)

print("Current hour is:", today)
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)
print(today.microsecond)
print(today.strftime("%Y-%m-%d %H:%M:%S"))
print(today.strftime("%A, %B %d, %Y"))
print(today.min)
print(today.max)