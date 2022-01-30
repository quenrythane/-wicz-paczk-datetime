import datetime

today = datetime.date.today()
print(today, "\n")

intDay = datetime.date(today.year, today.month, today.day).weekday()
days = ['pn', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']

print(days[intDay])
print()