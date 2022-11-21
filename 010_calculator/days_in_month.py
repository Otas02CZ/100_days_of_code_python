# this app will tell you the number of days in a given month of a given year

from rich.prompt import IntPrompt

def is_leap(year : int) -> bool:
    """Returns True/False whether the year is a leap year"""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year : int, month : int) -> int:
    """Returns the number of days in the month of the given year"""
    days_in_months : list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return 0
    if is_leap(year):
        if month == 2:
            return days_in_months[month - 1] + 1
    return days_in_months[month - 1]


print("Welcome to the Days In Month calculator, gimme year and month and I will tell you the number of days.")
year : int = IntPrompt.ask("Insert the year as a number")
month : int = IntPrompt.ask("Insert the month as a number")
days : int = days_in_month(year, month)
if days == 0:
    print("You have inserted a bad value for the month")
else:
    print(f"There are {days} days in year {year} and month {month}.")