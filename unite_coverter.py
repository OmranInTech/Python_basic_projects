# Constants for menu options
MENU_PROMPT = """
Unit Converter
1. Length (Meter ↔ Kilometer)
2. Weight (Gram ↔ Kilogram)
3. Temperature (Celsius ↔ Fahrenheit)
4. Exit
"""
LENGTH, WEIGHT, TEMPERATURE, EXIT = "1", "2", "3", "4"
METERS_TO_KILOMETERS = "1"
KILOMETERS_TO_METERS = "2"
GRAMS_TO_KILOGRAMS = "1"
KILOGRAMS_TO_GRAMS = "2"
CELSIUS_TO_FAHRENHEIT = "1"
FAHRENHEIT_TO_CELSIUS = "2"

# Conversion functions for length
def meter_to_kilometer(meters: float) -> float:
    return meters / 1000

def kilometer_to_meter(kilometers: float) -> float:
    return kilometers * 1000

# Conversion functions for weight
def gram_to_kilogram(grams: float) -> float:
    return grams / 1000

def kilogram_to_gram(kilograms: float) -> float:
    return kilograms * 1000

# Conversion functions for temperature
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

# Helper function to get a valid float input from the user.
def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Functions for each conversion category
def convert_length():
    choice = input("Convert (1) Meter → Kilometer or (2) Kilometer → Meter? ")
    if choice == METERS_TO_KILOMETERS:
        meters = get_float_input("Enter meters: ")
        print(f"{meters} m = {meter_to_kilometer(meters)} km")
    elif choice == KILOMETERS_TO_METERS:
        kilometers = get_float_input("Enter kilometers: ")
        print(f"{kilometers} km = {kilometer_to_meter(kilometers)} m")
    else:
        print("Invalid option. Please enter 1 or 2.")

def convert_weight():
    choice = input("Convert (1) Gram → Kilogram or (2) Kilogram → Gram? ")
    if choice == GRAMS_TO_KILOGRAMS:
        grams = get_float_input("Enter grams: ")
        print(f"{grams} g = {gram_to_kilogram(grams)} kg")
    elif choice == KILOGRAMS_TO_GRAMS:
        kilograms = get_float_input("Enter kilograms: ")
        print(f"{kilograms} kg = {kilogram_to_gram(kilograms)} g")
    else:
        print("Invalid option. Please enter 1 or 2.")

def convert_temperature():
    choice = input("Convert (1) Celsius → Fahrenheit or (2) Fahrenheit → Celsius? ")
    if choice == CELSIUS_TO_FAHRENHEIT:
        celsius = get_float_input("Enter Celsius: ")
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
    elif choice == FAHRENHEIT_TO_CELSIUS:
        fahrenheit = get_float_input("Enter Fahrenheit: ")
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")
    else:
        print("Invalid option. Please enter 1 or 2.")

def choose_conversion_category():
    """Handles the high-level category selection and delegates to the appropriate function."""
    while True:
        print(MENU_PROMPT)
        choice = input("Select a conversion category (1-4): ").strip()
        
        if choice == LENGTH:
            convert_length()
        elif choice == WEIGHT:
            convert_weight()
        elif choice == TEMPERATURE:
            convert_temperature()
        elif choice == EXIT:
            print("Exiting the unit converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

# Run the converter application
if __name__ == "__main__":
    choose_conversion_category()
