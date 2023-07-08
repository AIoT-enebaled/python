# Import the randint function from the random module
from random import randint

# Define a list of options for the player to choose from
options = ["rock", "paper", "scissors"]

# Define a tuple of winning combinations
winning_combinations = ((0, 2), (1, 0), (2, 1))

# Print the starting message
print('Let\'s play rock paper scissors')

# Start a while loop to keep the game going until the player chooses to stop
while True:
    # Generate a random number between 0 and 2 (inclusive)
    x = randint(0, 2)
    
    # Ask the player to choose rock, paper, or scissors
    print('Choose one of the following options:')
    for i, option in enumerate(options):
        print(f"{i+1}: {option}")
    y = int(input()) - 1
    
    # Check if the player's choice is valid
    if y not in [0, 1, 2]:
        print('Invalid option, please choose again.')
        continue
    
    # Check the player's choice against the computer's choice
    if y == x:
        # If the choices match, it's a draw
        print(f"It's a draw, both chose {options[y]}. Let's play again!")
    elif (y, x) in winning_combinations:
        # If the player wins, display the winning message
        print(f"You win! {options[y].capitalize()} beats {options[x]}!")
    else:
        # If the computer wins, display the losing message
        print(f"You lose! {options[x].capitalize()} beats {options[y]}!")
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again != 'y':
        # If the player doesn't want to play again, exit the loop
        print("Thanks for playing!")
        break
