from setuptools import setup, find_packages

setup(
    name='hw-1',
    version='0.1.0',
    description='demo cli tool to remind you of birthdays',
    packages=find_packages(),
    install_requires=[
        "faker",
    ],
    author="Roman Slipchenko",
    author_email="romanslipchenko@gmail.com",
    entry_points={'console_scripts': [
        'birthdays-reminder = modules.birthdays_reminder.main:main',
        'bot-assistant = modules.bot_assistant.main:main']},
)
