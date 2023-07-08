import random

options = ["rock", "paper", "scissors"]
play_again = True

while play_again:
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    while player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(options)

    print(f"\nYou chose {player_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    else:
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")
            
    play_again_input = input("Do you want to play again? (Y/N)").lower()
    while play_again_input not in ["y", "n"]:
        print("Invalid input. Please enter Y or N.")
        play_again_input = input("Do you want to play again? (Y/N)").lower()
    if play_again_input == "n":
        play_again = False
        print("Thanks for playing!")
