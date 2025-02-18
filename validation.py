from utils import print_failure

def validate_book(book):
    if not book['title'].strip():
        print_failure('Book Title cannot be empty')
        return
    if not book['author'].strip():
        print_failure('Book author cannot be empty')
        return
    return True


def validate_member(member):
    if not member['member_id'].strip():
        print_failure('Member ID cannot be empty')
        return
    if not member['name'].strip():
        print_failure('Member Name cannot be empty')
        return
    return True   


