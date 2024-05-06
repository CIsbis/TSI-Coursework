from src.engine.board import print_board, is_board_full
from src.engine.game_logic import check_winner
from src.engine.input_validation import get_valid_input

def run_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        print("Welcome to Tic Tac Toe!")

        while True:
            print_board(board)
            row = get_valid_input(f"Player {current_player}, enter row (0, 1, or 2): ", [0, 1, 2])
            col = get_valid_input(f"Player {current_player}, enter column (0, 1, or 2): ", [0, 1, 2])

            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("That cell is already occupied. Try again.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    run_game()
