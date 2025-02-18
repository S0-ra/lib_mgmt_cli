from utils import *

class Member:

    @staticmethod
    def add_member(member):
        data=read_data()
        data['members'].append(member)
        write_data(data)

    @staticmethod
    def display_all_members():
        return read_data()['members']
        

        