def meter_to_kilometer(meters):
    return meters / 1000

def kilometer_to_meter(kilometers):
    return kilometers * 1000

def gram_to_kilogram(grams):
    return grams / 1000

def kilogram_to_gram(kilograms):
    return kilograms * 1000

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def get_float_input(prompt):
    """Helper function to get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def unit_converter():
    while True:
        print("\nUnit Converter")
        print("1. Length (Meter ↔ Kilometer)")
        print("2. Weight (Gram ↔ Kilogram)")
        print("3. Temperature (Celsius ↔ Fahrenheit)")
        print("4. Exit")
        
        choice = input("Select a conversion category (1-4): ")

        if choice == "1":
            sub_choice = input("Convert (1) Meter → Kilometer or (2) Kilometer → Meter? ")
            if sub_choice == "1":
                meters = get_float_input("Enter meters: ")
                print(f"{meters} m = {meter_to_kilometer(meters)} km")
            elif sub_choice == "2":
                kilometers = get_float_input("Enter kilometers: ")
                print(f"{kilometers} km = {kilometer_to_meter(kilometers)} m")
            else:
                print("Invalid option. Please enter 1 or 2.")

        elif choice == "2":
            sub_choice = input("Convert (1) Gram → Kilogram or (2) Kilogram → Gram? ")
            if sub_choice == "1":
                grams = get_float_input("Enter grams: ")
                print(f"{grams} g = {gram_to_kilogram(grams)} kg")
            elif sub_choice == "2":
                kilograms = get_float_input("Enter kilograms: ")
                print(f"{kilograms} kg = {kilogram_to_gram(kilograms)} g")
            else:
                print("Invalid option. Please enter 1 or 2.")

        elif choice == "3":
            sub_choice = input("Convert (1) Celsius → Fahrenheit or (2) Fahrenheit → Celsius? ")
            if sub_choice == "1":
                celsius = get_float_input("Enter Celsius: ")
                print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
            elif sub_choice == "2":
                fahrenheit = get_float_input("Enter Fahrenheit: ")
                print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")
            else:
                print("Invalid option. Please enter 1 or 2.")

        elif choice == "4":
            print("Exiting the unit converter. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")

# Run the converter
unit_converter()
