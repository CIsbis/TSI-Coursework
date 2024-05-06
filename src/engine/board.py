def print_board(board):
    for row in board:
        print(" | ".join(row))
        print(" -" * 5)


def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))
