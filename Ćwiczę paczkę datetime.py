import datetime


def todays_date():
    # zwraca dzisiejszą datę, np 2022-01-31
    today = datetime.date.today()  # -> 2022-01-31
    return today


# dzień miesiąca
def monthday():
    month_day = today.day  # -> 31
    return month_day


# zwraca dzień tygodnia
def weekday():
    week_days_list = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    day_of_week = today.weekday() # -> 0
    if week_days_list[day_of_week][-1] == 'a':
        return week_days_list[day_of_week].replace('a', 'ę')
    else:
        return week_days_list[day_of_week]


# zwraca miesiąc
def month():
    months_list = ['pusty' ,'Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']  # pusty bo datetime numeruje od 1
    month = today.month  # -> 1
    return months_list[month]


# zwraca rok
def year():
    year = today.year
    return year


# łącze poprzednie
def message_with_todays_date_connected():
    full_message = (f'Dziś mamy {weekday()}, {monthday()} {month()} {year()} rok')
    return full_message

today = datetime.date.today()
print(todays_date())
print(monthday())
print(weekday())
print(month())
print(year())
print(message_with_todays_date_connected())
