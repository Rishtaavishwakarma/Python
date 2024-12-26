import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move(board):
    return random.choice(get_empty_positions(board))

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    print("Here's the board:")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:  # Player's turn
            print("Your turn!")
            row, col = player_move(board)
            board[row][col] = "X"
        else:  # Computer's turn
            print("Computer's turn!")
            row, col = computer_move(board)
            board[row][col] = "O"

        print_board(board)

        if turn >= 4:  # Check for a winner after 5 moves
            if check_winner(board, "X"):
                print("Congratulations! You win!")
                break
            elif check_winner(board, "O"):
                print("Computer wins! Better luck next time.")
                break
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
