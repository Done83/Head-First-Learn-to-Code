# Random lib import
import random

#  Winner variable set up
winner = ''

# Computers random choice of rock, paper or scissors
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

# Users input, rock, paper or scissors
users_choice = input("rock, paper or scissors? ")
while (users_choice != 'rock' and users_choice != 'paper' and users_choice!= 'scissors'):
    users_choice = input("rock, paper or scissors? ")


# Game logic to determine the winner
if computer_choice == users_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and users_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and users_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and users_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

# Displaying the winnner at the end
if winner == 'Tie':
    print(f"We both chose {computer_choice}, play again.")
else:
    print(f"{winner}, won, I chose {computer_choice}")
