import json

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    print("-" * 40)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print("-" * 40)

def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    found_contacts = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"- {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']} | Address: {contact['address']}")
    else:
        print("No matching contacts found.")

def update_contact(contacts):
    search_contact(contacts)
    try:
        index = int(input("\nEnter the number of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Enter new details (leave blank to keep current value):")
            contact = contacts[index]
            name = input(f"Name ({contact['name']}): ").strip() or contact['name']
            phone = input(f"Phone ({contact['phone']}): ").strip() or contact['phone']
            email = input(f"Email ({contact['email']}): ").strip() or contact['email']
            address = input(f"Address ({contact['address']}): ").strip() or contact['address']
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_contact(contacts):
    search_contact(contacts)
    try:
        index = int(input("\nEnter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("==========================")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
