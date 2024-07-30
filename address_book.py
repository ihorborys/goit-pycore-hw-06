from collections import UserDict
from record import Record


class AddressBook(UserDict):

    def add_record(self, name):
        record = None
        if not self.find(name):
            record = Record(name)
            self[name] = record
            print("Record added successfully")
        else:
            print("Record already exists")
        return record

    def find(self, name):
        return self.get(name)

    def delete(self, name):
        if self.find(name):
            self.pop(name)
            print("Record deleted successfully")
        else:
            print("Record does not exists")

    def __str__(self):
        records = ""
        for name in self:
            records += f"{self[name]}\n"
        return records
