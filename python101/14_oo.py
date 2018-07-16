# EXAMPLEs...

# Contact:
#     (attributes/fields, properties...)
#     name
#     phonenumber
class Contact:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def __str__(self):
        return self.name + "  " + self.phonenumber

    # def __repr__(self):
    #     return str(self)


class AddressBook:
    def __init__(self):
        self.contacts_info = {}

    def add_user(self, name, phone):
        c = Contact(name, phone)
        self.contacts_info[name] = c
    
    def exists(self, name):
        return name in self.contacts_info
    
    # implement __str__ for addressbook.
    # implement edit_user
    # implement delete_user
    # implement search
    # implement list_users
    
Addressbook:
    contacts_info

    behavior: (methods)
        add_user
        delete_user
        search_user
        edit_user

