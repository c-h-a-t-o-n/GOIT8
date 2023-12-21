from datetime import date, datetime


def get_birthdays_per_week(users):
    result = {}

    # Словник для відповідності чисел дням тижня
    DAYS_OF_WEEK = {
        0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
        4: "Friday", 5: "Saturday", 6: "Sunday"
    }

    if not users:
        return result

    today = date.today()
    this_year = today.year

    # Перебір користувачів для знаходження найближчих днів народження
    for user in users:
        # Заміна року народження користувача на поточний рік
        user_birthday_in_this_year = user["birthday"].replace(year=this_year)
        user_birthday_in_next_year = user["birthday"].replace(year=this_year + 1)

        delta_1 = (user_birthday_in_this_year - today).days
        delta_2 = (user_birthday_in_next_year - today).days

        # Визначення найближчого дня народження
        if 0 <= delta_1 < 7:
            user_closest_birthday = user_birthday_in_this_year
        elif delta_1 < 0 and delta_2 < 7:
            user_closest_birthday = user_birthday_in_next_year
        else:
            continue

        # Визначення дня тижня для найближчого дня народження
        user_closest_birthday_day = user_closest_birthday.weekday()
        user_closest_birthday_day = 0 if user_closest_birthday_day >= 5 else user_closest_birthday_day

        # Додавання імен користувачів до відповідного дня тижня
        result.setdefault(DAYS_OF_WEEK[user_closest_birthday_day], []).append(user["name"])

    return result


if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Olivia", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Jan", "birthday": datetime(1955, 1, 3).date()},
        {"name": "Lily", "birthday": datetime(1984, 12, 30).date()},
    ]

    result = get_birthdays_per_week(users)

    # Displaying the result
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
