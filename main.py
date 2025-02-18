from utils import *
from validation import *
from book import Book
from member import Member
import time

def display_menu():
    print_title("Library Management System\n")
    print_option("1. Add New Book")
    print_option("2. Display All Books")
    print_option("3. Search for Book")
    print_option("4. Add New Member")
    print_option("5. Display All Members")
    print_option("0. Exit")
    print()

def handle_choice(choice):
    clear_screen()
    if choice == '1':
        add_new_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        add_new_member()
    elif choice == '5':
        display_members()
    elif choice == '0':
        print_success("Exiting system......")
        time.sleep(2)
        return False
    else:
        print_failure("Invalid choice. Please try again.")
    input("Press any key to continue...")
    return True

def add_new_book():
    print_title("Adding New Book : \n")
    title=user_prompt('Enter book title : ')
    author=user_prompt('Enter author name : ')
    try:
        quantity=int(user_prompt('Enter quantity : '))
    except ValueError:
        print_failure('Quantity must be a valid integer')
        return
        
    book = {
        #generating BookID in the format B001,B012, etc
        "book_id": f"B{len(read_data()['books']) + 1:03}",
        "title": title,
        "author": author,
        "quantity": quantity
    }

    #validate book data
    if validate_book(book) is not True:
        print_failure(f"Book validation failed. Please check your input")
        return
    
    #check if the book title is unique
    if not Book.check_unique_boook_title(book['title']):
        print_failure("Book title already exists. Cannot add the same book again")
        return

    #add the book
    Book.add_book(book)
    print_success(f"Book '{title}' added successfull\n")

def search_book():
    print_title('Search Book by Title : \n')
    title = user_prompt("Enter book title to search: ")
    book = Book.search_book(title)
    if book:
        print_success(f"\nBook Found: {book['title']} by {book['author']} (Quantity: {book['quantity']})\n")
    else:
        print_failure("\nBook not found\n")

def add_new_member():
    print_title('Adding New Member : \n')
    name = user_prompt("Enter member name: ")
    member_id = user_prompt("Enter member ID: ")

    member = {
        "member_id": member_id,
        "name": name
    }

    #validate member data
    if validate_member(member) != True:
        print_failure(f"\nMember validation failed. Please check your input\n")
        return

    #check if the member ID is unique
    if not Member.check_unique_member_id(member_id):
        print_failure("\nMember ID already exists. Cannot add the same member again\n")
        return

    #add the member
    Member.add_member(member)
    print_success(f"\nNew member : {name} added successfully.\n")

def display_books():
    print_title("List of Books : ")
    print('\n')
    books = Book.display_all_books()
    if books:
        for book in books:
            print(f"Book : {book['title']}\nAuthor: {book['author']}\nQuantity : {book['quantity']}\n")
    else:
        print_failure("No books available in the library.\n")

def display_members():
    print_title('List of Members : \n')
    members=Member.display_all_members()
    if members:
        for member in members:
            print(f"Member_ID : {member['member_id']}\nName : {member['name']}\n")
    else:
        print_failure("No members available in the library.\n")

def main():
    while True:
        clear_screen()
        display_menu()
        choice=input("Enter your choice : ")
        if not handle_choice(choice):
            break


if __name__=='__main__':
    main()