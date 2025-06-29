#random password genrator 
import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage
password = generate_password(16)  # Change the number to adjust the length
print(f"Generated Password: {password}")
