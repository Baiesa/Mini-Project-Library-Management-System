# here is my all functions 

import re
from classes import Book,User,Genre,Author
def validate_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Display")
    print("6. Quit")

    choice = validate_input("Enter your choice: ", r"[1-5]")
    return int(choice)

def book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

    choice = validate_input("Enter your choice: ", r"[1-5]")
    return int(choice)

def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

    choice = validate_input("Enter your choice: ", r"[1-3]")
    return int(choice)

def author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

    choice = validate_input("Enter your choice: ", r"[1-3]")
    return int(choice)

def genre_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")

    choice = validate_input("Enter your choice: ", r"[1-3]")
    return int(choice)

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    genre = input("Enter the genre of the book: ")
    publication_date = input("Enter the publication date of the book: ")

    return Book(title, author, isbn, genre, publication_date)

def add_user():
    name = input("Enter the name of the user: ")
    library_id = input("Enter the library ID of the user: ")

    return User(name, library_id)

def add_author():
    name = input("Enter the name of the author: ")
    biography = input("Enter the biography of the author: ")

    return Author(name, biography)

def add_genre():
    name = input("Enter the name of the genre: ")
    description = input("Enter the description of the genre: ")
    category = input("Enter the category of the genre: ")

    return Genre(name, description, category)