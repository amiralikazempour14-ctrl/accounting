book = {}


def normalize_name(name):
    return name.strip().lower()


def phone_valid(number):
    return len(number) == 11 and number.isdigit()


def add_contact(book, name, phone, group):
    book[normalize_name(name)] = {
        "phone": phone,
        "group": group
    }


def search_contact(book, name):
    return book.get(normalize_name(name))


def delete_contact(book, name):
    key = normalize_name(name)

    if key in book:
        book.pop(key)
        return True

    return False


def list_contacts(book):
    return sorted(book)


while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        group = input("Enter group: ")

        if normalize_name(name) == "":
            print("Name cannot be empty")
            continue

        if not phone_valid(phone):
            print("Phone must be 11 digits")
            continue

        add_contact(book, name, phone, group)
        print("Contact added")

    elif choice == "2":
        name = input("Enter name: ")
        contact = search_contact(book, name)

        if contact is None:
            print("Contact not found")
        else:
            print(f"Phone: {contact['phone']}")
            print(f"Group: {contact['group']}")

    elif choice == "3":
        name = input("Enter name: ")

        if delete_contact(book, name):
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "4":
        names = list_contacts(book)

        if len(names) == 0:
            print("No contacts found")
        else:
            for i, name in enumerate(names, start=1):
                print(f"{i}. {name} | {book[name]['phone']} | {book[name]['group']}")

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")