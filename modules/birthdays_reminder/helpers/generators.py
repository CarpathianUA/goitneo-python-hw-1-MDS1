from faker import Faker
from datetime import datetime, time


def generate_users(num_users):
    fake = Faker()
    users_list = []

    for _ in range(num_users):
        name = fake.name()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)
        birthday_datetime = datetime.combine(birthday, time())
        user_data = {"name": name, "birthday": birthday_datetime}
        users_list.append(user_data)

    return users_list


if __name__ == "__main__":
    users_by_day = generate_users(100)
