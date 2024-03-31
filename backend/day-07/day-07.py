# Rasty Espartero | BSCS 2-4 | Backend Department
# Day 07 Entry

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

def view_list():
    print("Your shopping list:")
    for item in shopping_list:
        print(item)

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")

while True:
    print("\nOptions:")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        item = input("Enter the item you want to add: ")
        add_item(item)
    elif choice == '2':
        view_list()
    elif choice == '3':
        item = input("Enter the item you want to remove: ")
        remove_item(item)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
