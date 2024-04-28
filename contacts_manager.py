contacts = []

def add_contact(name, phone_number):
    contact = {'name': name, 'phone_number': phone_number}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

def remove_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' removed successfully.")
            return
    print(f"Contact '{name}' not found.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone Number: {contact['phone_number']}")
