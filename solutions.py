import math
import datetime

def get_year():
    """
    This function is given to you... it is used by the is_leap_year() function below.
    Do not modify this function.
      :returns: The current year, e.g. 2020
    """
    now = datetime.datetime.now()  # get the current time now
    year = now.year  # the current year
    return year

def is_square():
    width = float(input("Enter the width of the area in inches: "))
    height = float(input("Enter the height of the area in inches: "))
    return width == height

def get_greatest():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 > num2:
        return num1
    else:
        return num2

def get_bmi_category():
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
    bmi = 703 * weight / (height ** 2)
    if bmi < 15:
        return "Very severely underweight"
    elif 15 <= bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Moderately obese"
    elif 35 <= bmi < 40:
        return "Severely obese"
    else:
        return "Very severely obese"

def get_discount():
    quantity = int(input("How many masks would you like to buy? "))
    price_per_mask = 5
    total_cost = quantity * price_per_mask
    if quantity >= 5000:
        total_cost *= 0.8
    return f"${int(total_cost):,}"

def is_leap_year():
    year = get_year()
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False
