from name import Name
from phone import Phone


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if not new_phone.value:
            print("Phone format is not valid")
            return

        if not self.find_phone(new_phone.value):
            self.phones.append(new_phone.value)
            print("Phone added successfully")
        else:
            print("Phone already exists")

    def remove_phone(self, phone: str):
        removed_phone = Phone(phone)
        if not removed_phone.value:
            print("Phone format is not valid")
            return

        if self.find_phone(removed_phone.value):
            self.phones.remove(removed_phone.value)
            print("Phone removed successfully")
        else:
            print("Phone does not exist")

    def edit_phone(self, current_phone: str, new_phone: str):
        current = Phone(current_phone)
        new = Phone(new_phone)
        if not current.value or not new.value:
            print("Phone format is not valid")
            return

        if current.value == new.value:
            print("Entered phones are equal")
            return

        if self.find_phone(new.value):
            print("New phone already exists")
            return

        if self.find_phone(current.value):
            index = self.phones.index(current.value)
            self.phones[index] = new.value
            print("Phone edited successfully")
        else:
            print("Phone does not exist")

    def find_phone(self, phone: str):
        found_phone = None
        if phone in self.phones:
            index = self.phones.index(phone)
            found_phone = self.phones[index]
        return found_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"