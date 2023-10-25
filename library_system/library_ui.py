# library_ui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import main  # Assuming main.py contains the functions for the library operations


import members as member
import books as book


def register_member():
    # Call the function to register a member
    name = simpledialog.askstring("Input", "Enter your name: ")
    member.register_member(name)
    messagebox.showinfo("Success", "Member was registered")


def borrow_book():
    # Call the function to borrow a book
    book_borrow = simpledialog.askstring("Input", "Enter book's title: ")
    if book_borrow:
        if book.borrow_book(book_borrow):
            messagebox.showinfo("Success", "Book was successfully borrowed ")
        else:
            messagebox.showwarning("Warning", "Book entered is not available")


def return_book():
    # Call the function to return a book
    book_back = simpledialog.askstring("Input", "Enter book's title: ")
    if book_back:
        if book.return_book(book_back):
            messagebox.showinfo("Success", "Your Book was returned")
        else:
            messagebox.showwarning("Warning", "Book doesn't exist or it was already returned ")


def display_books():
    # Call the function to display all books
    messagebox.showinfo("Books Info", book.dict_books)


def display_members():
    # Call the function to display all members
    messagebox.showinfo("Members Info", member.library_members)


def add_book():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            book.add_book(title, author)  # Using the function from books.py
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


def exit_program():
    if messagebox.askokcancel("Exit", "Do you want to exit the program?"):
        root.destroy()


root = tk.Tk()
root.title("Library Management System")
root.title("Exit Button")

# Menu buttons
add_book_btn = tk.Button(root, text="Add a new book", command=add_book)
add_book_btn.pack(pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=register_member)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrow_book)
borrow_book_btn.pack(pady=10)

return_book_btn = tk.Button(root, text="Return a book", command=return_book)
return_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=display_books)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=display_members)
display_members_btn.pack(pady=10)

exit_button_btn = tk.Button(root, text="Exit", command=exit_program)
exit_button_btn.pack(pady=10)

root.mainloop()
