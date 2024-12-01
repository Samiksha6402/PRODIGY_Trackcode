#Contact Management
import json
import os
import re

CONTACTS_FILE = "contacts.json"
PHONE_REGEX = r"^\d{10}$"
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def validate_phone(phone):
    if re.fullmatch(PHONE_REGEX, phone):
        return True
    print("Invalid phone number. It should be 10 digits.")
    return False


def validate_email(email):
    if re.fullmatch(EMAIL_REGEX, email):
        return True
    print("Invalid email address. Please provide a valid email.")
    return False


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    while not validate_phone(phone):
        phone = input("Enter a valid phone number: ").strip()
    email = input("Enter email address: ").strip()
    while not validate_email(email):
        email = input("Enter a valid email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Current details: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    phone = input("Enter new phone number (leave blank to keep current): ").strip()
    if phone:
        while not validate_phone(phone):
            phone = input("Enter a valid phone number (leave blank to keep current): ").strip()
        contacts[name]['phone'] = phone
    email = input("Enter new email address (leave blank to keep current): ").strip()
    if email:
        while not validate_email(email):
            email = input("Enter a valid email address (leave blank to keep current): ").strip()
        contacts[name]['email'] = email
    print(f"Contact '{name}' updated successfully.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    print(f"Contact '{name}' deleted successfully.")


def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
