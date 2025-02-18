import json
import os

file_name='library_data.json'
CYAN='\033[1;36m'
PURPLE='\033[1;35m'
RED='\033[1;31m'
GREEN='\033[1;32m'
LIGHT_GRAY = "\033[0;37m"
RESET='\033[0m'

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


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def print_color_text(color,text):
    print(f"{color}{text}{RESET}")

def print_title(text):
    return print_color_text(CYAN,text)

def print_option(text):
    return print_color_text(PURPLE,text)

def print_success(text):
    return print_color_text(GREEN,text)

def print_failure(text):
    return print_color_text(RED,text)

def user_prompt(prompt):
    return input(f"{LIGHT_GRAY}{prompt}{RESET}")