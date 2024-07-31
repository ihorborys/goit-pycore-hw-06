from address_book import AddressBook


def main():
    book = AddressBook()

    john = book.add_record("John")
    john.add_phone('0931151222')
    john.add_phone('0931156692')

    alex = book.add_record("Alex")
    alex.add_phone('0931199999')
    alex.add_phone('0931156688')
    alex.edit_phone('0931156688', '0931111999')

    tom = book.add_record("Tom")
    tom.add_phone('0931199999')
    tom.add_phone('0931156688')
    tom.add_phone('0631112238')
    tom.remove_phone('0931156688')
    tom.remove_phone('0931199999')
    tom.remove_phone('0931999559')
    print(book)


if __name__ == "__main__":
    main()
