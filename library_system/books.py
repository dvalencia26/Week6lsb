dict_books = {"title": ["To Kill a Mockingbird"], "author": ["Harper Lee"], "availability": [True]}
library_books = [dict_books]


def add_book(title, author):
    dict_books["title"].append(title)
    dict_books["author"].append(author)
    dict_books["availability"].append(True)


def borrow_book(title):
    for i in range(len(dict_books["title"])):
        if dict_books["title"][i] == title and dict_books["availability"][i]:
            dict_books["availability"][i] = False
            return False


def return_book(title):
    for i in range(len(dict_books["title"])):
        if dict_books["title"][i] == title and not dict_books["availability"][i]:
            dict_books["availability"][i] = True
            return True


def find_book(title):
    for i in range(len(dict_books["title"])):
        if dict_books["title"][i] == title:
            return "Book's Author: " + dict_books["author"][i] + " Book's availability: " + str(dict_books["availability"][i])


'''
title_ex = input("Write book's title: ")
author_ex = input("Write author's name: ")

print(add_book(title_ex, author_ex))
print(library_books)
print("Borrow book", borrow_book(title_ex))
print("Return Book", return_book(title_ex))
print("Find book", find_book(title_ex))


'''