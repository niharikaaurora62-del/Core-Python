import datetime

today = datetime.date.today()
dob = datetime.date(1998, 7, 23)

year = today.year - dob.year
month = today.month - dob.month
day = today.day - dob.day
day_day = dob.strftime("%A")
print("Your Age is " , year,"Years", month, "Months", day, "Days" , "And you were born on", day_day)
day_month = dob.strftime("%B")
print(day_month)
day_datetime = dob.strftime("%c")
print(day_datetime)
day_date = dob.strftime("%d")
print(day_date)