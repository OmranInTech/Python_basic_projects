
def is_palindrome(text: str) -> str:
    """
    Checks if the given text is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring spaces and case.

    Args:
        text (str): The input string to check.

    Returns:
        str: Result message indicating whether the input is a palindrome.
    """
    # Normalize the input: remove spaces and convert to lowercase
    normalized_text = text.lower().replace(" ", "")
    
    # Reverse the normalized text
    reversed_text = normalized_text[::-1]
    
    # Check if the text is a palindrome
    if normalized_text == reversed_text:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"


# Example usage
if __name__ == "__main__":
    print(is_palindrome("abca"))
