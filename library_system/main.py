from books import add_book, borrow_book, return_book, find_book, dict_books
from members import register_member, find_member, library_members


def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Write book's title: ")
            author = input("Write author's name: ")
            add_book(title, author)
            pass
        elif choice == "2":
            name = input("Enter your name: ")
            register_member(name)
            pass
        elif choice == "3":
            book_title = input("What book you would like to borrow ?(Enter book's title): ")
            borrow_book(book_title)
            pass
        elif choice == "4":
            book_return = input("What's the title of the book you would to return? ")
            return_book(book_return)
            pass
        elif choice == "5":
            # Call function to display all books
            print(dict_books)
            pass
        elif choice == "6":
            # Call function to display all members
            print(library_members)
            pass
        elif choice == "7":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

