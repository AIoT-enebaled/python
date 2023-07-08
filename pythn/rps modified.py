import random
import sys


# Define the valid options and the winning combinations
options = ["rock", "paper", "scissors"]
winCombo = ((0,2),(1,0),(2,1))
# Initialize global variables for player score, computer score, and round count
player_score = 0    
computer_score = 0
round_count = 1

def main():
    # Prompt the user to choose a difficulty level
    print('Welcome! dear friend to :\n')
    print("RPS Royale Rumble \n")
    print("Let's get started..................\n")
    print("Choose from the options below::::: \n")
    
    difficulty = getDifficulty()
    setAI(difficulty)
    while True:
        # Prompt the user to choose the number of rounds to play
        num_rounds = getNumRounds()
        # Play the specified number of rounds
        playRounds(num_rounds)
        # Display the final score and the winner
        print(f"Final score: Player {player_score} - {computer_score} Computer")
        if player_score > computer_score:
            print("Congratulations, you won!, \n")
        elif computer_score > player_score:
            print("Sorry, the computer won, You're sick, kid\n")
        else:
            print("It's a tie!")
            print("You can do better than this!\n")
        # Ask the user if they want to play again
        if not playAgain():
            print("Thank you for playing RPS Royale Rumble!")
            sys.exit()

def getDifficulty():
    # Prompt the user to choose a difficulty level and return the chosen level
    difficulty = int(input('1) Easy 2) Medium 3) Hard: '))
    return difficulty

def setAI(difficulty):
    # Set the difficulty level by adjusting the probability that the computer wins each round
    global probability_computer_wins
    if difficulty == 1:
        probability_computer_wins = 0.5
    elif difficulty ==2:
        probability_computer_wins = 0.3
    elif difficulty == 3:
        probability_computer_wins = 0.25

def getNumRounds():
    # Prompt the user to choose the number of rounds to play and return the chosen number
    num_rounds = int(input("How many rounds do you want to play? \n"))
    return num_rounds

def makeMove():
    # Prompt the user to choose an option and choose a random option for the computer
    global player_choice, computer_choice
    player_choice = input("Choose rock, paper or scissors: \n")
    while player_choice not in options:
        player_choice = input("Invalid choice. Choose rock, paper or scissors: \n")
    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}\n")

def checkResult():
    # Determine the winner of the round and update the player and computer scores
    global player_score, computer_score
    if player_choice == computer_choice:
        print("It's a tie!!!\n")
        print("You can do better than this!\n")
    elif (options.index(player_choice), options.index(computer_choice)) in winCombo:
        print("You won!, I didn't know you are so smart \n")
        player_score += 1
    else:
        print("Computer won! \n")
        print("You are just an Idiot, you can't beat me, am the 'KING' in this Challange :)\n")
        computer_score += 1

def playRounds(num_rounds):
    # Play the specified number of rounds
    global player_score, computer_score, round_count
    player_score = 0
    computer_score = 0
    round_count = 1
    for i in range(num_rounds):
        print(f"Round {round_count}\n")
        makeMove()        
        checkResult()
        round_count += 1
    print(f"Final score: Player {player_score} - {computer_score} Computer\n")

def playAgain():
    # Prompt the user to play again and return True if they choose to play again, False otherwise
    while True:
        play_again = input("Play again? (y/n):\n ")
        if play_again.lower() == "n":
            return False
        elif play_again.lower() == "y":
            return True
        else:
            print("Invalid input.\n")

if __name__ == '__main__':
    main()
    

#"RPS Royale Rumble"

