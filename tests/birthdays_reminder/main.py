from tests.birthdays_reminder.test_generate_users_by_day import test_generate_users
from tests.birthdays_reminder.test_get_birthdays_per_week import test_get_birthdays_per_week


if __name__ == "__main__":
    test_generate_users()
    test_get_birthdays_per_week(100)

    print("All tests passed!")
