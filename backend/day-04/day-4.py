Player1 = 'Rock'
Player2 = 'Rock'

if Player1 == 'Rock' and Player2 == 'Scissors':
    print(f'Player1 wins!')
elif Player1 == 'Rock' and Player2 == 'Paper':
    print(f'Player2 wins!')
elif Player1 == Player2:
    print('It\'s a draw')
else:
    print(f'Player2 wins!')
