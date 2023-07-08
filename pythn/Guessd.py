import random

def play_game():
    max_attempts = 5
    range_min = 1
    range_max = 100

    print(f"I'm thinking of a number between {range_min} and {range_max}.")
    print(f"You have {max_attempts} attempts to guess the number.")

    number = random.randint(range_min, range_max)

    for attempt in range(max_attempts):
        guess = int(input("Enter your guess: "))

        if guess < range_min or guess > range_max:
            print(f"Your guess should be between {range_min} and {range_max}.")
            continue

        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print(f"Congratulations! You guessed the number in {attempt + 1} attempts.")
            return

    print(f"Sorry, you ran out of attempts. The number was {number}.")

play_again = 'y'

while play_again == 'y':
    play_game()
    play_again = input("Would you like to play again? (y/n)").lower()

print("Thank you for playing! Have a great day!")
