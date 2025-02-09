def bmi_cal():
    height_input_cm = float(input('Enter Your Height in centimeters: '))  # Height in cm
    weight_input = float(input('Enter your weight in kilograms: '))  # Weight in kg

    # Convert height from cm to meters
    height_input_m = height_input_cm / 100

    # BMI formula
    bmi_re = weight_input / (height_input_m ** 2)
    print('Your BMI is: ', round(bmi_re, 2))

    # BMI categorization
    if bmi_re < 18.5:
        print('You are underweight!')
    elif 18.5 <= bmi_re < 24.9:
        print('You have a normal weight!')
    elif 25 <= bmi_re < 29.9:
        print('You are overweight!')
    else:
        print('You are obese!')

bmi_cal()
