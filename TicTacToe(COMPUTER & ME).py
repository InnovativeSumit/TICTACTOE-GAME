import random

#THIS GAME IS PLAYED BY COMPUTER AND YOU
def print_board(board):
    """Prints the current state of the board."""
    print("\n" + "\n".join([" | ".join(row) for row in board]))
    print()


def check_winner(board, player):
    """Checks if the current player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    """Checks if the board is full."""
    return all(cell in ['X', 'O'] for row in board for cell in row)


def get_empty_cells(board):
    """Returns a list of empty cells."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']


def minimax(board, depth, is_maximizing):
    """Minimax algorithm to determine the best move."""
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for (r, c) in get_empty_cells(board):
            board[r][c] = 'O'
            score = minimax(board, depth + 1, False)
            board[r][c] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (r, c) in get_empty_cells(board):
            board[r][c] = 'X'
            score = minimax(board, depth + 1, True)
            board[r][c] = ' '
            best_score = min(score, best_score)
        return best_score


def best_move(board):
    """Finds the best move for the AI."""
    best_score = -float('inf')
    move = None
    for (r, c) in get_empty_cells(board):
        board[r][c] = 'O'
        score = minimax(board, 0, False)
        board[r][c] = ' '
        if score > best_score:
            best_score = score
            move = (r, c)
    return move


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # 'X' is the human player

    while True:
        print_board(board)

        if current_player == 'X':
            # Human player's turn
            while True:
                try:
                    row = int(input("Enter the row (0, 1, or 2): "))
                    col = int(input("Enter the column (0, 1, or 2): "))
                    if (row, col) in get_empty_cells(board):
                        board[row][col] = 'X'
                        break
                    else:
                        print("Cell already taken or invalid. Choose another cell.")
                except ValueError:
                    print("Invalid input. Please enter numbers 0, 1, or 2.")
        else:
            # AI's turn
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
            else:
                print("No valid moves left for AI.")

        # Check for a winner
        if check_winner(board, 'X'):
            print_board(board)
            print("Player X wins!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("Player O wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()

