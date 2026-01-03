import csv
import os

FILE_NAME = "contacts.csv"

# Ensure CSV file exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])

# Add new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print("✅ Contact added successfully!\n")

# View all contacts
def view_contacts():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print("\n--- Contact List ---")
        for row in reader:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
        print()

# Search contact
def search_contact():
    keyword = input("Enter name or phone to search: ").strip()

    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if keyword.lower() in row[0].lower() or keyword in row[1]:
                print(f"Found → Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                found = True

    if not found:
        print("❌ Contact not found.\n")

# Update contact
def update_contact():
    name_to_update = input("Enter contact name to update: ").strip()
    updated_contacts = []
    updated = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_contacts.append(header)

        for row in reader:
            if row[0].lower() == name_to_update.lower():
                print("Enter new details:")
                row[1] = input("New Phone: ")
                row[2] = input("New Email: ")
                updated = True
            updated_contacts.append(row)

    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_contacts)

    if updated:
        print("✅ Contact updated successfully!\n")
    else:
        print("❌ Contact not found.\n")

# Delete contact
def delete_contact():
    name_to_delete = input("Enter contact name to delete: ").strip()
    remaining_contacts = []
    deleted = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        remaining_contacts.append(header)

        for row in reader:
            if row[0].lower() != name_to_delete.lower():
                remaining_contacts.append(row)
            else:
                deleted = True

    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(remaining_contacts)

    if deleted:
        print("🗑️ Contact deleted successfully!\n")
    else:
        print("❌ Contact not found.\n")

# Main Menu
def main():
    initialize_file()

    while True:
        print("📒 CONTACT BOOK")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
