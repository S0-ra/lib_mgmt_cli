from utils import read_data,write_data
from validation import *

class Book:

    @staticmethod
    def search_book(book_title):
        if book_title.isspace():
            return None
        books=read_data()['books']
        for book in books:
            if book_title.lower() == book['title'].lower():
                return book
        return None
            
    @staticmethod
    def add_book(book):
        data = read_data()
        
        print(f"\nAdding new book {book['title']} by {book['author']}\n")
        data['books'].append(book)

        write_data(data)


    @staticmethod
    def display_all_books():
        return read_data()['books']
    
    @staticmethod
    def check_unique_boook_title(book_title):
        books=read_data()['books']
        for book in books:
           if book['title']==book_title:
                return False
        return True

