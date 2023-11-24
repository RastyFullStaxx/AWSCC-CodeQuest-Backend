import random

# Variables
askName = input("Hey there, what's your name?: ")
response= input(f'Sup {askName}, wanna play-rock-paper, scissors?: ').lower().strip()

# Playing 
if response == 'yes':
    print("\nGreat! Let's start")
    
    print('\nJack..and POY!')
    
    main_list = ['rock', 'paper', 'scissors']
    random.shuffle(main_list)
    player1 = random.choice(main_list)
    player2 = random.choice(main_list)
    
    print(f'\n{askName} with "{player1}" ..   vs   .. Me with a "{player2}"')
    
    if player1 == 'rock' and player2 == 'scissors':
        print('\nDanggg.. You win!!')
    elif player1 == 'rock' and player2 == 'paper':
        print('\nHa! In your face!')
    elif player2 == 'rock' and player2 == 'scissors':
        print('\nHa! In your face!')
    elif player2 == 'rock' and player2 == 'paper':
        print('\nDanggg.. You win!!')
    elif player1 == 'scissors' and player2 == 'rock':
        print('\nHa! In your face!')
    elif player1 == 'rock' and player2 == 'scissors':
        print('\nDanggg.. You win!!')
    elif player1 == player2:
        print('\nWell.. a draw it is!')
    
else:
    print(f'\nReally? What a shame.. Have a good day bro {askName}!')
    
print('\n\n\n\n\n\n\n')