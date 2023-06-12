def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[9][9] == player:
        return True
    if board[0][9] == board[1][1] == board[9][0] == player:
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter the row (0-9): "))
        col = int(input("Enter the column (0-9): "))

        if row < 0 or row > 9 or col < 0 or col > 9:
            print("Invalid input! Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already occupied! Try again.")
            continue

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

play_game()
