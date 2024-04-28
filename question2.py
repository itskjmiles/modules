import contacts_manager

def main():
    while True:
        print("\nContact List Manager")
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. Display all contacts")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            contacts_manager.add_contact(name, phone_number)
        elif choice == '2':
            name = input("Enter name of contact to remove: ")
            contacts_manager.remove_contact(name)
        elif choice == '3':
            contacts_manager.display_contacts()
        elif choice == '4':
            print("Exiting the Contact List Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
