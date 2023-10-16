from modules.birthdays_reminder.helpers.validators import validate_birthdays_result


def format_birthday_result(birthdays):
    result = str()
    try:
        if not birthdays:
            return "No birthdays this week."
        if isinstance(birthdays, dict) and validate_birthdays_result(birthdays):
            for day, names in birthdays.items():
                result += f"{day}: {', '.join(names)}\n"
        else:
            result = birthdays
        return result
    except TypeError as e:
        return f"Error: {e}"
