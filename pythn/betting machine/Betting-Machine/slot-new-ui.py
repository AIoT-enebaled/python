import tkinter as tk
from tkinter import messagebox
import random
import winsound

# Create the main window
window = tk.Tk()
window.title("Slot Machine Game")
window.geometry("400x400") # Set the size of the window

# Constants and variables initialization
MAX_LINES = 3
MAX_BET = 1000000
MIN_BET = 1000

# Define symbols count and their respective values
symbols_count = {
    "A": 4,
    "B": 6,
    "C": 8,
    "D": 10,
}

symbol_value = {
    "A": 10,
    "B": 8,
    "C": 6,
    "D": 4,
}

# Initialize variables
balance = 0
total_bet = 0
total_lost = 0

# Function to spin the slot machine
def spin():
    # Play spin sound effect
    winsound.PlaySound("spin.wav", winsound.SND_ASYNC)
    
    # Get user input
    lines_input = lines_entry.get()
    bet_input = bet_entry.get()
    
    # Check if lines and bet inputs are empty
    if not lines_input or not bet_input:
        messagebox.showerror("Invalid Input", "You must enter the number of lines and bet amount to continue playing.")
        return
    
    # Convert input to integers
    lines = int(lines_input)
    bet = int(bet_input)

    # Validate user input
    if lines < 1 or lines > MAX_LINES:
        messagebox.showerror("Invalid Input", f"Number of lines must be between 1 and {MAX_LINES}.")
        return
    if bet < MIN_BET or bet > MAX_BET:
        messagebox.showerror("Invalid Input", f"Bet amount must be between {MIN_BET} and {MAX_BET}.")
        return

    global balance, total_bet, total_lost

    # Calculate total bet
    total_bet += bet * lines

    # Check if user has sufficient funds
    if total_bet > balance:
        messagebox.showerror("Insufficient Funds", "You have insufficient funds. Please deposit more money.")
        return

    # Generate random spin result
    spin_result = []
    for _ in range(lines):
        symbols = list(symbols_count.keys())
        spin_line = [random.choice(symbols) for _ in range(3)]
        spin_result.append(spin_line)

    # Update UI with spin result
    update_spin_result(spin_result)

    # Check winnings
    total_winnings, winning_lines = check_winnings(spin_result, lines, bet, symbol_value)

    # Update balance and UI
    balance -= bet * lines
    balance += total_winnings
    
    # Update total lost
    total_lost += bet * lines - total_winnings
    
    balance_label.config(text=f"Balance: Ugx {balance}")
    
    if total_winnings > 0:
        messagebox.showinfo("Result", f"You won Ugx {total_winnings}.\nWinning lines: {winning_lines}")

# Function to check if a player has won and returns total winnings and winning lines
def check_winnings(spin_result, lines, bet, symbol_value):
    total_winnings = 0
    winning_lines = []
    
    # Check rows
    for line in range(lines):
        symbols = spin_result[line]
        symbol = symbols[0]
        count = 1
        
        for i in range(1, 3):
            if symbols[i] == symbol:
                count += 1
            else:
                break
        
        if count == 3:
            total_winnings += symbol_value[symbol] * bet
            winning_lines.append(f"Row {line + 1}")
    
    # Check columns
    for col in range(3):
        symbol = spin_result[0][col]
        count = 1
        
        for i in range(1, lines):
            if spin_result[i][col] == symbol:
                count += 1
            else:
                break
        
        if count == lines:
            total_winnings += symbol_value[symbol] * bet
            winning_lines.append(f"Column {col + 1}")
    
    return total_winnings, winning_lines

# Function to update the spin result in the UI
def update_spin_result(spin_result):
    for i, spin_line in enumerate(spin_result):
        line_label = line_labels[i]
        
        for j, symbol in enumerate(spin_line):
            symbol_label = symbol_labels[i][j]
            symbol_image = symbol_images[symbol]
            symbol_label.config(image=symbol_image)
        
        line_label.config(text=" | ".join(spin_line))

# Function to deposit money into the game
def deposit():
    global balance
    deposit_amount = int(deposit_entry.get())
    
    if deposit_amount > 0:
        balance += deposit_amount
        balance_label.config(text=f"Balance: Ugx {balance}")
        messagebox.showinfo("Deposit", f"Ugx {deposit_amount} deposited successfully.")
    else:
        messagebox.showerror("Invalid Amount", "Deposit amount must be greater than 0.")

# Function to withdraw money from the game
def withdraw():
    global balance
    withdraw_amount = int(withdraw_entry.get())
    
    if withdraw_amount > 0 and withdraw_amount <= balance:
        balance -= withdraw_amount
        balance_label.config(text=f"Balance: Ugx {balance}")
        messagebox.showinfo("Withdraw", f"Ugx {withdraw_amount} withdrawn successfully.\nNew Balance: Ugx {balance}")
    else:
        messagebox.showerror("Invalid Amount", "Withdraw amount must be greater than 0 and less than or equal to your current balance.")

# Create UI elements
welcome_label = tk.Label(window, text="Welcome to the Lucky Slots Adventure!\n", fg="blue", font=("Times New Roman", 14, "bold"))
welcome_label.pack(pady=10)


balance_label = tk.Label(window, text="Balance: Ugx 0",fg="red", font=("Times New Roman", 10, "bold"))
balance_label.pack(pady=10)

deposit_label = tk.Label(window, text="Deposit Amount:",fg="blue", font=("Times New Roman", 10, "bold"))
deposit_label.pack()

deposit_entry = tk.Entry(window,fg="red", font=("Times New Roman", 10, "bold"))
deposit_entry.pack()

deposit_button = tk.Button(window, text="Deposit", command=deposit, background="blue", foreground="white",fg="red", font=("Times New Roman", 10, "bold"))
deposit_button.pack(pady=10)

withdraw_label = tk.Label(window, text="Withdraw Amount:",fg="red", font=("Times New Roman", 10, "bold"))
withdraw_label.pack()

withdraw_entry = tk.Entry(window,fg="blue", font=("Times New Roman", 10, "bold"))
withdraw_entry.pack()

withdraw_button = tk.Button(window, text="Withdraw", command=withdraw, background="blue", foreground="white",fg="black", font=("Times New Roman", 10, "bold"))
withdraw_button.pack(pady=10)

lines_label = tk.Label(window, text="Number of Lines (1-3):",fg="purple", font=("Times New Roman", 8, "bold"))
lines_label.pack()

lines_entry = tk.Entry(window,fg="blue", font=("Times New Roman", 8, "bold"))
lines_entry.pack()

bet_label = tk.Label(window, text="Bet Amount:",fg="blue", font=("Times New Roman", 8, "bold"))
bet_label.pack()

bet_entry = tk.Entry(window,fg="red", font=("Times New Roman", 8, "bold"))
bet_entry.pack()

spin_button = tk.Button(window, text="Spin", command=spin, background="blue", foreground="white")
spin_button.pack(pady=10)

close_button = tk.Button(window, text="Close",fg="red", font=("Times New Roman", 10, "bold"), command=window.destroy)
close_button.pack(pady=10)

line_labels = []
symbol_labels = []

# Load symbol images
symbol_images = {}
for symbol in symbols_count.keys():
    symbol_image = tk.PhotoImage(file=f"{symbol}.png")
    # Reduce image size by a factor of 4
    symbol_image = symbol_image.subsample(4, 4)
    symbol_images[symbol] = symbol_image

for _ in range(MAX_LINES):
    line_frame = tk.Frame(window)
    line_frame.pack()
    
    line_symbol_labels = []
    
    for _ in range(3):
        symbol_label = tk.Label(line_frame)
        symbol_label.pack(side=tk.LEFT)
        line_symbol_labels.append(symbol_label)
    
    symbol_labels.append(line_symbol_labels)
    
    line_label = tk.Label(line_frame, text="")
    line_label.pack()
    line_labels.append(line_label)

# Run the main window loop
window.mainloop()
