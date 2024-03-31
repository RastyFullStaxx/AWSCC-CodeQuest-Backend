import json
import os

def print_menu():
    menu = ["1 - Add Username, Email, and Password for a Website",
            "2 - View all inputs",
            "3 - Search for a specific input",
            "4 - Delete an existing input",
            "5 - Update a specific input",
            "6 - Exit"]
    
    for item in menu:
        print(item)

def check_input(choice):
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        website = input("Enter website: ")
        search(website)
    elif choice == "4":
        website = input("Enter website: ")
        delete(website)
    elif choice == "5":
        website = input("Enter website: ")
        update(website)
    elif choice == "6":
        exit()

def is_existing(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        return website in data

def add():
    website = input("Enter website: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    new_data = {
        website: [{
            'email': email,
            'password': password
        }]
    }

    with open('data.json', 'r') as f:
        data = json.load(f)
    
    if website in data:
        data[website].append({'email': email, 'password': password})
    else:
        data.update(new_data)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    os.system('cls')
    print("Successfully added!")
    
def view():
    os.system('cls')
    with open('data.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            print(f"Website: {key}")
            for item in val:
                print(f"    Email: {item['email']}")
                print(f"    Password: {item['password']}\n")

def search(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        if website in data:
            print(f"Website: {website}")
            for item in data[website]:
                print(f"    Email: {item['email']}")
                print(f"    Password: {item['password']}\n")
        else:
            print("No entries found for this website.")

def delete(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        if website in data:
            del data[website]
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Entry deleted successfully.")
        else:
            print("No entries found for this website.")

def update(website):
    with open('data.json', 'r') as f:
        data = json.load(f)
        if website in data:
            email = input("Enter new email: ")
            password = input("Enter new password: ")
            data[website] = [{'email': email, 'password': password}]
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Entry updated successfully.")
        else:
            print("No entries found for this website.")

running = True

while running:
    print("======= PASSWORD MANAGER =======")
    print_menu()
    user_input = input("Enter a number: ")
    check_input(user_input)
