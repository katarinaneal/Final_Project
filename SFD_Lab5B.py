def print_board(board):
    for row in reversed(board):
        for cell in row:
            print(cell, end=' ')
        print()
    print()

def initialize_board(num_rows, num_cols):
    return [["-" for _ in range(num_cols)] for _ in range(num_rows)]

def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return row

def check_if_winner(board, col, row, chip_type):
    # Check horizontally
    count = 0
    for c in range(len(board[0])):
        if board[row][c] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertically
    count = 0
    for r in range(len(board)):
        if board[r][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False

def main():
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    print()

    board = initialize_board(height, length)
    print_board(board)

    print("Player 1: x")
    print("Player 2: o")

    player = 1

    while True:
        col = input(f"\nPlayer {player}: Which column would you like to choose? ")
        try:
            col = int(col)
        except ValueError:
            print("Invalid input! Please enter a valid column number.")
            continue

        if 0 <= col < length:
            row = insert_chip(board, col, 'x' if player == 1 else 'o')
            print_board(board)
            if check_if_winner(board, col, row, 'x' if player == 1 else 'o'):
                print(f"\nPlayer {player} won the game!")
                break
            elif all(board[i][j] != "-" for i in range(height) for j in range(length)):
                print("\nDraw. Nobody wins.")
                break
            else:
                player = 3 - player
        else:
            print("Invalid column! Please choose a column within the board dimensions.")
            continue

if __name__ == "__main__":
    main()