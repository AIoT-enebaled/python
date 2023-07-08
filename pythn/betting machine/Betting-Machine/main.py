#Importing necessary modules
import random
import time



#Constants and variables initialization
MAX_LINES = 3
MAX_BET = 1000000
MIN_BET = 1000

ROWS = 3
COLS = 3

#Symbols count and their respective values
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

#Function to check if a player has won and returns total winnings and winning lines
def check_winnings(columns, lines, bet, values):
    total_winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        count = 1
        for column in range(1, len(columns)):
            if columns[column][line] == symbol:
                count += 1
            else:
                break
        if count == len(columns):
            total_winnings += symbol_value[symbol] * bet
            winning_lines.append(line + 1)
    return total_winnings, winning_lines

#Function to get random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

#Function to print slot machine spin
def print_slot_machine_spin(columns):
    for row in range (len (columns[0])):
        for i, column in enumerate (columns):
            if i != len (columns) - 1:
                print (column[row], end=" | ")
            else:
                print (column[row], end="")
                
        print()
           
            
#Function to deposit money into the game
def deposit():
    while True:
        amount = input("How much would you like to deposit? \nUgx:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0\n")
                continue
        else:
            print("Amount must be a number\n")
            continue
        
#Function to get the bet amount from the player        
def get_bet():
    while True:
        amount = input("How much would you like to bet? \nUgx:")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f" Enter a valid amount between \nUgx:{MIN_BET} and {MAX_BET}")
                continue
        else:
            print("Please enter a number\n")
            continue 
        
# Function to get number of lines to bet on     
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on: (1-3))\n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid of number lines")
                continue
        else:
            print("Please enter a number")
            continue

#Function to play the game and returns the net winnings or loss of the player            
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You have insufficient funds, please deposit more money.\n")
            deposit_amount = deposit()
            balance += deposit_amount
            continue
        else:
            break
    print(f"You are betting Ugx {bet} on {lines} lines. Total bet is \nUgx: {total_bet}.")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won Ugx {winnings}.\n")
    print("You won on lines:\n", *winning_lines)
    
    return winnings - total_bet

def withdraw(balance):
    while True:
        amount = input("How much would you like to withdraw? \nUgx:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and amount <= balance:
                return amount
            elif amount <= 0:
                print("Amount must be greater than 0.\n")
                continue
            else:
                print("Insufficient funds. Please enter a valid amount.\n")
                continue
        else:
            print("Invalid input. Please enter a number.\n")
            continue



def main():
    balance = deposit()

    while True:
        print(f"Your current balance is \nUgx: {balance}\n")
        action = input("Choose an action: (P)lay, (W)ithdraw, (Q)uit: \n")

        if action.lower() == "p":
            balance += spin(balance)
        elif action.lower() == "w":
            withdrawal_amount = withdraw(balance)
            balance -= withdrawal_amount
            print(f"You have withdrawn Ugx {withdrawal_amount}.\n")
        elif action.lower() == "q":
            print(f"Your balance is Ugx {balance}\n")
            print("Thank you for playing!\n")
            break
        else:
            print("Invalid input. Please choose a valid action.\n")
            continue
main()
        