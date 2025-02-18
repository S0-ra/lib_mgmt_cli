from utils import *

class Book:

    @staticmethod
    def search_book(book_title):
        if book_title.isspace():
            return None
        books=read_data()['books']
        for book in books:
            if book_title.lower() == book['title'].lower():
                return book
            
    @staticmethod
    def add_book(book):
        data=read_data()
        existing_book=Book.search_book(book['title'])
        if(existing_book):
            existing_book['quantity']+=book['quantity']
        else:
            data['books'].append(book)
        write_data(data)

    @staticmethod
    def display_all_books():
        return read_data()['books']
