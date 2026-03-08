WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def create_board():
    return [" "] * 9


def render_board(board):
    rows = []
    for start in range(0, 9, 3):
        row = " | ".join(board[start:start + 3])
        rows.append(f" {row} ")
    return "\n-----------\n".join(rows)


def display_board(board):
    print(render_board(board))


def get_available_moves(board):
    return [index for index, value in enumerate(board) if value == " "]


def is_valid_move(board, move):
    return move in get_available_moves(board)


def apply_move(board, move, marker):
    board[move] = marker


def check_winner(board):
    for a, b, c in WIN_LINES:
        line = board[a], board[b], board[c]
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
    return None


def is_draw(board):
    return check_winner(board) is None and not get_available_moves(board)


def board_positions_guide():
    guide = [str(index + 1) for index in range(9)]
    return render_board(guide)
