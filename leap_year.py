"""
Leap Year Checker Module

Provides a function to determine if a given year is a leap year,
with robust CLI support and unit tests.
"""

from typing import Any


def is_leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year, False otherwise.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_year_from_user(prompt: str = "Enter a year: ") -> int:
    """
    Prompts the user for a year and validates input.

    Args:
        prompt (str): The prompt message to display.

    Returns:
        int: The validated year input by the user.
    """
    while True:
        try:
            year_str = input(prompt)
            year = int(year_str)
            if year <= 0:
                raise ValueError("Year must be positive.")
            return year
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer.")


def main() -> None:
    """
    Main function to execute when script is run directly.
    """
    year = get_year_from_user()
    if is_leap_year(year):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")


if __name__ == "__main__":
    main()


# Unit tests
import unittest

class TestLeapYear(unittest.TestCase):
    def test_leap_years(self):
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(1600))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2019))
        self.assertFalse(is_leap_year(1))

if __name__ == "__main__":
    unittest.main(exit=False)
