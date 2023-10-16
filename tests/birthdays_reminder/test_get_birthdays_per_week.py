from modules.birthdays_reminder.helpers.generators import generate_users
from modules.birthdays_reminder.get_birthdays import get_birthdays_per_week


def test_get_birthdays_per_week(num_users):
    users = generate_users(num_users)

    result = get_birthdays_per_week(users)

    assert isinstance(result, dict)
    print("test: get birthdays per week: passed!")
