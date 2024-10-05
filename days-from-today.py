from datetime import datetime

def get_days_from_today(date): # '2020-10-09'
    fmt = "%Y-%m-%d"
    try:
        date = datetime.strptime(date, fmt)
        today = datetime.now()
        return (today - date).days
    except ValueError:
        print(f"date format must match {fmt}, was {date}")
        return -1

# print(get_days_from_today("2024f2f-10-02"))