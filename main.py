import calendar
from collections import defaultdict
from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    completed_data = defaultdict(list)
    date_today = date.today()
    for user in users:
        for defined_year in [date_today.year, date_today.year + 1]:
            if date_today <= (users_bd := user["birthday"].replace(
                    year=defined_year)) <= date_today + timedelta(weeks=1):
                wd = "Monday" if (wd := calendar.day_name[
                    users_bd.weekday()]) in {"Saturday", "Sunday"} else wd
                completed_data[wd].append(user["name"])
    return completed_data


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

