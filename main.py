
# This is my main menu to call the classes and functions 

from classes import *
from menu_actions import *

while True:
    choice = main_menu()

    if choice == 1: 
        book_choice = book_menu()
        if book_choice == 1: 
            book = add_book()
            print("New book added:", book)

    elif choice == 2: 
        user_choice = user_menu()
        if user_choice == 1:  
            user = add_user()
            print("New user added:", user.name)

    elif choice == 3: 
        author_choice = author_menu()
        if author_choice == 1: 
            author = add_author()
            print("New author added:", author.name)
    
    elif choice == 4: 
        genre_choice = genre_menu()
        if genre_choice == 1:  
            genre = add_genre()
            print("New genre added:", genre.name)
   
    elif choice == 5: 
        print("Thank you for using the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")