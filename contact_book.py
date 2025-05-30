#contact book

def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search a contact")
    print("4. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact_book[name] = {"Phone": phone, "Email": email}
    print(f"Contact for {name} added successfully!")

def view_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

def search_contact(contact_book):
    name = input("Enter the name to search: ")
    if name in contact_book:
        details = contact_book[name]
        print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print("Contact not found.")

def main():
    contact_book = {}  # Store contacts in a dictionary
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
