from utils import write_data,read_data

class Member:

    @staticmethod
    def add_member(member):
        data=read_data()
        data['members'].append(member)
        write_data(data)

    @staticmethod
    def display_all_members():
        return read_data()['members']
    
    @staticmethod
    def check_unique_member_id(member_id):
        members=read_data()['members']
        for member in members:
            if member['member_id']==member_id:
                return False
        return True

        