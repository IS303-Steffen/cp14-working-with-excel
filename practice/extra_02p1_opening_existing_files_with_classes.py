# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

'''
Write a program that can do the following:
    1. import books from excel sheet into book objects, all stored in a list
        Book objects should have instance variables that correspond to the excel sheet
    2. import borrowers from excel sheet into borrower objects, all stored in a list
        Borrower objects should have instance variables that correspond to the excel sheet,
        as well as an instance variable called "books_borrowed" that stores book objects they are borrowing
    3. Add any book objects that have a "borrowed by id" matching with a borrower be added to that 
        borrower's books_borrowed.
    4. Show all the available books
    5. Ask the user which book they want to check out
    6. Ask the user which user will check it out.
    7. Update the excel spreadsheet

'''
import openpyxl

class Book:
    def __init__(self, book_id, title, author, borrowed_by_id):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed_by_id = borrowed_by_id

class Borrower:
    def __init__(self, borrower_id, name, email):
        self.borrower_id = borrower_id
        self.name = name
        self.email = email
        self.books_borrowed = []

    def borrow_book(self, book):
        if len(self.books_borrowed) < 3:
            self.books_borrowed.append(book)
        else:
            print("Can't borrow more than 3 books!")















