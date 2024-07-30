from address_book import AddressBook


def main():
    book = AddressBook()

    john = book.add_record("John")
    john.add_phone('0931151222')
    john.add_phone('0931156692')

    alex = book.add_record("Alex")
    alex.add_phone('0931199999')
    alex.add_phone('0931156688')

    tom = book.add_record("Tom")
    tom.add_phone('0931199999')
    tom.add_phone('0931156688')
    print(book)


if __name__ == "__main__":
    main()
