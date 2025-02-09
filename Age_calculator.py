import datetime

def age_cal(birthdate):
    # Convert the input string into a date object
    birth_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    
    # Get the current date
    current_date = datetime.datetime.now()
    
    # Calculate the age in years
    age_years = current_date.year - birth_date.year
    
    # Adjust the age if the current date is before the birthday this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age_years -= 1
    
    return age_years

# Take input in the format "YYYY-MM-DD"
age_input = input("Enter your DOB (YYYY-MM-DD): ")
age = age_cal(age_input)
print(f"Your age is: {age} years")
