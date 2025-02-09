class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'"{book_name}" has been added to the library.')

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'"{book_name}" has been removed from the library.')
        else:
            print(f'"{book_name}" is not in the library.')

    def display_books(self):
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(f'- {book}')
        else:
            print("The library is empty.")

if __name__ == "__main__":
    lib = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_name = input("Enter book name to add: ")
            lib.add_book(book_name)
        elif choice == "2":
            book_name = input("Enter book name to remove: ")
            lib.remove_book(book_name)
        elif choice == "3":
            lib.display_books()
        elif choice == "4":
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice, please try again.")
