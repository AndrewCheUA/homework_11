from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = value
    
    
class Name(Field):
    @property
    def value(self):
        return self._value
    
    @value.setter
    def set_value(self, item):
        self._value = item


class Phone(Field):
    @property
    def value(self):
        return self._value
    
    @value.setter
    def set_value(self, item):
        if item.startswith("+38") and len(item) == 13:
            self._value = item
        else:
            print("Incorrect phone number")


class Birthday(Field):
    @property
    def value(self):
        return self._value
    
    @value.setter
    def set_value(self, item):
        try:
            user_date = item.split()
            birthday = datetime(year = int(user_date[0]), month = int(user_date[1]), day = int(user_date[2]))
            self._value = birthday
        except:
            print("Invalid birthday format!")


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        
    def add_phone(self, item):
        phone = Phone(None)
        phone.set_value = item
        if phone.value != None:
            self.phones.append(phone)
        else:
            print("Phone was not added to record.") 

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def add_birthday(self, date_input):
        self.birthday = Birthday(None)
        self.birthday.set_value = date_input
        
    def show_all(self):
        print(self.phones)
        
       
class AddressBook(UserDict):
    def add_record(self, user_input):
        x = user_input.split()
        if len(x) == 3:
            y = Name(None)
            y.set_value = x[1]
            record = Record(name=y)
            record.add_phone(x[2])
            self.data[record.name.value] = record
        elif len(x) == 2:
            y = Name(None)
            y.set_value = x[1]
            record = Record(name=y)
            self.data[record.name.value] = record
        else:
            print("Incorrect command")
        birthday_input = input("Would you like to set birthday for the contact? ")
        if birthday_input.lower() == "yes":
            date_input = input("Please enter birthday (year month day):")
            record.add_birthday(date_input)
    
    def days_to_birthday(self, birthday):
        current_date = datetime.today()
        this_year_b = datetime(current_date.year, birthday.month, birthday.day)

        days_until_birthday = (this_year_b - current_date).days
        if days_until_birthday < 0:
            this_year_b = datetime(current_date.year + 1, birthday.month, birthday.day)
            days_until_birthday = (this_year_b - current_date).days
            return days_until_birthday
        else:
            return days_until_birthday
    
    def iterator(self, r_count):
        returned_records = []
        b_index = 0
        while r_count > 0 and r_count <= len(book):
            current_record = []
            record_x = book.get(list(self.data.keys())[(len(book) + b_index) - len(book)])
            r_count = r_count - 1
            current_record.append(record_x.name.value)
            phones = []
            for i in record_x.phones:
                phones.append(i.value)
            current_record.append(phones)
            try:
                current_record.append(str(f"Birthday: {record_x.birthday.value.date()}"))
            except:
                pass
            returned_records.append(current_record)
            b_index += 1
        return returned_records


book = AddressBook()

def quit_f(_=None):
    print("Good bye!")
    quit()

END_DICT = {'good bye':quit_f,
            'close':quit_f,
            'exit':quit_f}


def main_cli():           
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() == "hello":
                print("How can I help you?")
        
        elif user_input.lower().startswith("add"):
            book.add_record(user_input)
            print("Record was added.")
            
        elif user_input.startswith("new phone"):
            name_ch = input("Please enter contact name: ")
            phone = input("Please enter contact phone: ")
            if name_ch in book:
                book.get(name_ch).add_phone(phone)
                print("Phone was added.")
            else:
                print("No such contact in contacts list.")
        
        elif user_input.startswith("remove phone"):
            name_ch = input("Please enter contact name: ")
            phone = input("Please enter contact phone: ")
            if name_ch in book:
                book.get(name_ch).remove_phone(phone)
                print("Phone was removed.")
            else:
                print("No such contact in contacts list.")
                
        elif user_input.startswith("update phone"):
            name_ch = input("Please enter contact name: ")
            old_phone = input("Please enter contact old phone: ")
            new_phone = input("Please enter contact new phone: ")
            if name_ch in book:
                book.get(name_ch).remove(old_phone)
                book.get(name_ch).add_phone(new_phone)
                print("Record was updated.")
            else:
                print("No such contact in contacts list.")
        
        elif user_input.startswith("contact birthday"):
            name_ch = input("Please enter contact name: ")
            if name_ch in book:
                try:
                    print (f"There are {book.days_to_birthday(book.get(name_ch).birthday.value)} days lef until {book.get(name_ch).name.value}s birthday")
                except:
                    print("Birthday date is not set for this contact!")
            else:
                print("No such contact in contacts list.")
        elif user_input.startswith("show all"):
            book.show_all()

        elif user_input.startswith("show records"):
            count_input = int(input("How many records do you need? "))
            print(book.iterator(count_input))
        
        elif user_input in END_DICT:
                END_DICT[user_input]()
    
if __name__ == "__main__":
    main_cli()