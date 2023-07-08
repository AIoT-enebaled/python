import random
import time

MAX_LINES = 3
MAX_BET = 1000000
MIN_BET = 1000
COLS = 3
ROWS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C":6,
    "D":8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C":3,
    "D":2,
}

def check_winnings(columns, lines, bet, values):
    total_winnings = 0 
    winning_lines = []
    for line in range(lines):
        symbol = columns [0][line]
        count = 1
        for column in range(1, len(columns)):
            if columns[column][line] ==symbol:
                count +=1
            else:
                break
            if count == len(columns):
                total_winnings += symbol_value[symbol]
                