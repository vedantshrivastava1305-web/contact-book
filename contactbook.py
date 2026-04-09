# Contact Book using Dictionary

contact_book = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact_book[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

def view_contacts():
    if not contact_book:
        print("No contacts found.")
        return
    for name, details in contact_book.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contact_book:
        details = contact_book[name]
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contact_book[name] = {"phone": phone, "email": email}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
menu()