import datetime

today = datetime.date.today()
print(today, "\n")

intDay = datetime.date(today.year, today.month, today.day).weekday()
days = ['poniedziałek', 'wtorek', 'środę', 'czwartek', 'piątek', 'sobotę', 'niedzielę']

print(f'Dziś mamy {days[intDay]}')
