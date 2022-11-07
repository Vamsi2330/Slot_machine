import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

symbol_values = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_winnings(colums,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = colums[0][line]
        for column in colums:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols )
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row])
        print()

def Deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if(amount > 0):
                break
            else:
                print("Amount must be Greater than 0.")
        else:
            print("Please enter number only.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+") ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please Enter number only.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line ?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <=MAX_BET :
                break
            else:
                print(f"Amount must between ${MIN_BET}-${MAX_BET}!")
        else:
            print("Please Enter number only.")
    return amount

def game(balance):
    lines = get_number_of_lines()
    while True:
            Bet = get_bet()
            total_bet = Bet * lines

            if total_bet > balance:
                print(f"You do not have enough balance to bet. Your balance is {balance}")
            else:
                break


    print(f"You are betting {Bet} on {lines} lines. Total bet Equals to : ${total_bet}")
        
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,Bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"Yow won on lines : ",*winning_lines)
    return winnings - total_bet

def main():
    balance = Deposit()

    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press enter to play (q to exit).")
        if answer=="q":
            break
        balance += game(balance)

    print(f"You left with ${balance}")
    
main()