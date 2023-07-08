import random

def play_game():
    attempts = 0  # Variable to track the number of attempts
    max_attempts = 5  # Maximum number of attempts allowed
    range_min = 1  # Minimum number in the range
    range_max = 100  # Maximum number in the range

    print(f"I'm thinking of a number between {range_min} and {range_max}.")
    print(f"You have {max_attempts} attempts to guess the number.")

    number = random.randint(range_min, range_max)  # Generate a random number within the range

    while attempts < max_attempts:  # Loop until the maximum number of attempts is reached
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increment the attempts counter

        if guess < range_min or guess > range_max:  # Check if the guess is out of range
            print(f"Your guess should be between {range_min} and {range_max}.")
            continue  # Skip the rest of the loop and start the next iteration

        if guess > number:  # Check if the guess is higher than the target number
            print("Too high.")
        elif guess < number:  # Check if the guess is lower than the target number
            print("Too low.")
        else:  # The guess is correct
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return  # Exit the function

    print(f"Sorry, you ran out of attempts. The number was {number}.")

play_again = 'y'

while play_again == 'y':  # Loop to ask if the user wants to play again
    play_game()
    play_again = input("Would you like to play again? (y/n)").lower()

print("Thank you for playing! Have a great day!")
