from datetime import datetime


def validate_users_input_data(users):
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        if isinstance(name, str) and isinstance(birthday, datetime):
            return True
        else:
            raise TypeError(f"Error: Invalid data type for users - {name}, birthday: {birthday}")


def validate_birthdays_result(birthdays):
    if not isinstance(birthdays, dict):
        raise TypeError("Error: Invalid data type for birthdays. Birthdays must be a dictionary.")

    for day, names in birthdays.items():
        if not isinstance(day, str):
            raise TypeError(f"Error: Invalid data type for day '{day}'. Day must be a string.")

        if not isinstance(names, list):
            raise TypeError(f"Error: Invalid data type for names in '{day}'. Names must be a list.")

        for name in names:
            if not isinstance(name, str):
                raise TypeError(f"Error: Invalid data type for '{name}' in '{day}'. Name must be a string.")

    return birthdays
