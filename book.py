from utils import read_data,write_data
from validation import *

class Book:

    @staticmethod
    def search_book_by_title(book_title):
        if book_title.isspace() or not book_title:
            return None
        books=read_data()['books']
        matched_books=[]
        for book in books:
            if book_title.lower() in book['title'].lower():
                matched_books.append(book)
        return matched_books if matched_books else None
    
    @staticmethod
    def search_book_by_author(book_author):
        if book_author.isspace() or not book_author:
            return None
        books=read_data()['books']
        matched_books=[]
        for book in books:
            if book_author.lower() in book['author'].lower():
                matched_books.append(book)
        return matched_books if matched_books else None
            
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

