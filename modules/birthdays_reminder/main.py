from modules.birthdays_reminder.get_birthdays import get_birthdays_per_week
from modules.birthdays_reminder.helpers.formatters import format_birthday_result
from modules.birthdays_reminder.helpers.mock_data import users_list


def main():
    print("Generated users:")
    print(format_birthday_result(get_birthdays_per_week()))
    print("Real users:")
    print(format_birthday_result(get_birthdays_per_week(users_list)))


if __name__ == "__main__":
    main()
