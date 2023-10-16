from datetime import datetime, timedelta
from collections import defaultdict
from modules.birthdays_reminder.constants.weekend_days import WEEKEND_DAYS
from modules.birthdays_reminder.helpers.generators import generate_users
from modules.birthdays_reminder.helpers.validators import validate_users_input_data


def get_birthdays_per_week(users=None):
    if users is None:
        users = generate_users(100)

    try:
        birthdays = process_users(users)
        return birthdays
    except (TypeError, ValueError) as e:
        return f"Error: {e}"


def process_users(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    if validate_users_input_data(users):
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date()

            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                # If the birthday has already passed this year, use next year
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            # Set the time of day to midnight - avoid offsets due to time zone or daylight saving time changes
            birthday_day = today + timedelta(days=delta_days, hours=0, minutes=0, seconds=0)

            # Check if the day falls within a week ahead from today.
            if delta_days < 7:
                if birthday_day.weekday() in WEEKEND_DAYS:
                    day_to_say_happy_birthday = "Monday"
                elif birthday_day.weekday() == today.weekday():
                    day_to_say_happy_birthday = "Today"
                else:
                    day_to_say_happy_birthday = birthday_day.strftime("%A")

                birthdays[day_to_say_happy_birthday].append(name)

    return birthdays
