contacts = {}

while True:
    print("\n📒 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("✅ Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\n📋 Contact List")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print(f"📞 {name}: {contacts[name]}")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("🗑️ Contact deleted successfully!")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")
