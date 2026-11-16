import numpy as np

board = np.zeros((3, 3), dtype=int)


def print_board(b):
    symbols = {0: ' ', 1: 'X', -1: 'O'}
    for r in range(3):
        row = " | ".join(symbols[val] for val in b[r])
        print(f" {row} ")
        if r < 2:
            print("-----|-----|-----")


def check_winner(b):
    for i in range(3):
        if np.all(b[i] == 1) or np.all(b[:, i] == 1):
            return "X"
        if np.all(b[i] == -1) or np.all(b[:, i] == -1):
            return "O"

    if np.all(np.diag(b) == 1) or np.all(np.diag(np.fliplr(b)) == 1):
        return "X"
    if np.all(np.diag(b) == -1) or np.all(np.diag(np.fliplr(b)) == -1):
        return "O"

    if not np.any(b == 0):
        return "Draw"

    return None



def read_move(player):
    while True:
        try:
            value = input(f"{player} Enter row and column (0,1,2): ")
            parts = value.split()

            if len(parts) == 2:
                row, col = map(int, parts)
            elif len(parts) == 1:
                row = int(parts[0])
                col = int(input(f"{player} Enter column (0,1,2): "))
            else:
                raise ValueError
        except ValueError:
            print("Please enter a number only.\n")
            continue

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Row and Column must be between 0 and 2.")
            continue

        if board[row, col] != 0:
            print("Cell already taken.")
            continue

        return row, col


current = 1
print("Welcome to Tic Tac Toe")
print_board(board)

while True:
    player = 'X' if current == 1 else 'O'
    row, col = read_move(player)

    board[row, col] = current
    print_board(board)

    result = check_winner(board)
    if result == "Draw":
        print("Ohoo, it's a Draw")
        break
    if result is not None:
        print(f"{result} Wins")
        break
    
    current *= -1

        