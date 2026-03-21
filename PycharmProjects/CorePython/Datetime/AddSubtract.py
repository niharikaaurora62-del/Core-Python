import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days=10)
past = today + datetime.timedelta(days=-10)

print("today is " + str(today))
print("future is " + str(future))
print("past is " + str(past))