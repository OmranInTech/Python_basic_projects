def bmi_cal():
    # Prompt the user to enter their height in centimeters and convert the input to a float
    height_input_cm = float(input('Enter Your Height in centimeters: '))  # Height in cm

    # Prompt the user to enter their weight in kilograms and convert the input to a float
    weight_input = float(input('Enter your weight in kilograms: '))  # Weight in kg

    # Convert the height from centimeters to meters for BMI calculation
    height_input_m = height_input_cm / 100

    # Calculate BMI using the formula: weight (kg) / (height (m))^2
    bmi_re = weight_input / (height_input_m ** 2)

    # Print the calculated BMI rounded to 2 decimal places
    print('Your BMI is: ', round(bmi_re, 2))

    # Classify the BMI result into categories based on standard BMI ranges
    if bmi_re < 18.5:
        print('You are underweight!')
    elif 18.5 <= bmi_re < 24.9:
        print('You have a normal weight!')
    elif 25 <= bmi_re < 29.9:
        print('You are overweight!')
    else:
        print('You are obese!')

# Call the bmi_cal function to run the BMI calculator
bmi_cal()
