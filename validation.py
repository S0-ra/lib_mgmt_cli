import jsonschema
from jsonschema.exceptions import ValidationError
import schema

def validate_data(data,schema):
    try:
        jsonschema.validate(instance=data,schema=schema)
        return True
    except ValidationError as e:
        return f"Validation failed : {e.message}"


def validate_book(book):
    return validate_data(book,schema.BOOK_SCHEMA)


def validate_member(member):
    return validate_data(member,schema.MEMBER_SCHEMA)
    


