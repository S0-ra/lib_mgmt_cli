import json
import os

file_name='library_data.json'

def read_data():
    if not os.path.exists(file_name):
        return {'books':[],
            'members':[]}
    try:
        with open(file_name,'r') as file:
            data=json.load(file)
    except Exception as e:
        return{
            'books':[],
            'members':[]
        }
    return data

def write_data(data):
    with open(file_name,'w') as file:
        json.dump(data,file,indent=4) 

def add_member(data,member):
    data['members'].append(member)
    write_data(data)

def check_unique_boook_title(book_title):
    books=read_data()['books']
    for book in books:
        if book['title']==book_title:
            return False
    return True

def check_unique_member_id(member_id):
    members=read_data()['members']
    for member in members:
        if member['member_id']==member_id:
            return False
    return True