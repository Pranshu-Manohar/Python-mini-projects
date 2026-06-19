contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")

        numbers = set(contacts.values())

        if number in numbers:
            print("Duplicate number detected")
        else:
            contacts[name] = number
            print("Contact added")

    elif choice == "2":
        name = input("Enter name: ")

        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter name: ")

        if name in contacts:
            contacts[name] = input("Enter new number: ")
            print("Contact updated")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "5":
        if contacts:
            for name, number in contacts.items():
                print(name, ":", number)
        else:
            print("No contacts available")

    elif choice == "6":
        break

    else:
        print("Invalid choice")