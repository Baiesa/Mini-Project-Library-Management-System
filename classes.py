
# the classes 
class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    
class Library:
    def __init__(self):
        self.books = []






class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability:
            book.availability = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available for borrowing")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.availability = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"'{book.title}' is not borrowed by {self.name}")

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category