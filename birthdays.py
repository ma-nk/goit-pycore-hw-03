from datetime import datetime, timedelta

def move_to_next_monday(date):
    # Get the weekday: Monday is 0 and Sunday is 6
    weekday = date.weekday()
    if weekday == 5:  # Saturday
        return date + timedelta(days=2)
    elif weekday == 6: # Sunday
        return date + timedelta(days=1)
    else:
        return date  # already a weekday

def get_upcoming_birthdays(users):
    ret = []
    today = datetime.today().date()
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday_this_year = datetime(today.year, user_birthday.month, user_birthday.day).date()
        if 7 > (user_birthday_this_year - today).days > 0:
            congratulation_date = move_to_next_monday(user_birthday_this_year)
            ret.append({"name" : user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return ret

users = [
    {"name": "John Doe", "birthday": "1985.10.06"},
    {"name": "Jane Smith", "birthday": "1990.10.05"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)