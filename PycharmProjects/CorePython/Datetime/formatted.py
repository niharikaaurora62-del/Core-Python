import  datetime

today =datetime.date.today()
formated = today.strftime("%d-%m-%y")
print("Real Date", today)
print("Formatted date:", formated)
