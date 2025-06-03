#leap year

def leap_year_checker(year):
    # Check if year is divisible by 4 and not divisible by 100 or divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if leap_year_checker(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
