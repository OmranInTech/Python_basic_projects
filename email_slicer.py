def email_slicer(email):
    # Split the email address at '@'
    username, domain = email.split('@')
    
    # Print the results
    print(f"Username: {username}")
    print(f"Domain: {domain}")

# Example usage:
email = input("Enter your email: ")
email_slicer(email)
