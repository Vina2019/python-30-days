import json

FILE = "contacts.json"

# Load existing contacts
try:
    with open(FILE, "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = []
except json.JSONDecodeError:
    print("Warning: contacts.json is corrupted. Starting with an empty contact list.")
    contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1" :
        name = input("Enter your contact name : ")
        phone = input("Enter phone no : ")

        contact = {
            "name" : name,
            "phone" : phone
        }

        contacts.append(contact)
        print("contact added ..!!")

    elif choice == "2":
        if not contacts:
            print("No contact found")
        else:
             for c in contacts:
                 print(c["name"],"-",c["phone"])

    elif choice == "3":
        search = input("Search a name : ")
        found = False

        for c in contacts :
            if c["name"].lower() == search :
                print("Found",c["name"],"-",c["phone"])

        if not found :
            print("Contact not found")

    elif choice == "4":
        with open(FILE,"w") as f:
            json.dump(contacts,f,indent = 4)
        print("Good bye")
        break     
    else :
        print("Invalid option")