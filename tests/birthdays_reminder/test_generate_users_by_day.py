from modules.birthdays_reminder.helpers.generators import generate_users
from datetime import date


def test_generate_users():
    num_users_to_test = 100
    users = generate_users(num_users_to_test)

    assert len(users) == num_users_to_test, f"Expected {num_users_to_test}, got {len(users)}"

    for user in users:
        # Check the structure of user data
        assert "name" in user, f"User data missing 'name': {user}"
        assert "birthday" in user, f"User data missing 'birthday': {user}"

        # Check the data types
        assert isinstance(user["name"], str), f"Name is not a string: {user['name']}"
        assert isinstance(user["birthday"], date), f"Birthday is not a datetime: {user['birthday']}"

    print("test: generate users: passed!")
