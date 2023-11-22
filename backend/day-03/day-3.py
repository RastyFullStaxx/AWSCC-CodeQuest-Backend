# Variables
name = 'Rasty'
weather = 'sunny'

# Greetings
print(f"Hey there {name}, we're having such a nice {weather} weather today aren't we?")
answer1 = input().strip().lower() 

# Response
if answer1 == "yes":
    print("\nYep, so what're you feeling today?")
else:
    print("\nNot a good talker, but anyway!\nWhat're you feeling today?")

# Feeling Selection
feeling = int(input("1. Productive \n2. Lazy \nSelect a number: "))

# Course of action
if feeling == 1:
    answer2 = input("\nGreat! I have some perfect lessons for your Python grind today, would you like to take them out? ").strip().lower()
else:
    print("\nWelp, can't help that. Let's wind down and do nothing for the rest of the day to help you relax!")

# Course of action 2
if answer2 == 'yes' or 'sure':
    print(f"\n{name} proceeds to code and learn!")
else:
    print("\nWelp, can't help that. Let's wind down and do nothing for the rest of the day to help you relax!")
