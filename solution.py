from datetime import datetime

def get_days_from_today(date): # '2020-10-09'
    date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.now()
    return (today - date).days


# print(get_days_from_today("2020-10-09"))