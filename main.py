def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    print("Adding a new contact...")
    print(f"Contact added: {name}, {phone}, {email}\n")


def remove_contact():
    print("Removing a contact...")
    # You can add actual removal logic here later


def list_contacts(contact_count):
    print("No contacts found.")
    print("Do you want to add a contact?")
    print("1. Yes")
    print("2. No")
    choice = int(input("Enter your choice: "))
    if choice == 2:
        add_contact()
        if contact_count == 0:
            pass
        else:
            print("Listing all contacts...")


def main():
    print("=== CONTACT ===")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. List Contacts")
    print("4. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if ch == 1:
        add_contact()
    elif ch == 2:
        remove_contact()
    elif ch == 3:
        list_contacts(0)
    elif ch == 4:
        print("Exiting...")
        exit()
    else:
        print("Invalid choice!! Please try again :)")

if __name__ == "__main__":
    main()
