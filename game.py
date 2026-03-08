# All row, column, and diagonal combinations that count as a win.
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

EMPTY_CELL = " "
BOARD_SIZE = 9
ROW_SIZE = 3
ROW_SEPARATOR = "\n-----------\n"


def create_board():
    return [EMPTY_CELL] * BOARD_SIZE


def render_board(board):
    rows = []
    for start in range(0, BOARD_SIZE, ROW_SIZE):
        cells = board[start:start + ROW_SIZE]
        row = " | ".join(cells)
        rows.append(f" {row} ")
    return ROW_SEPARATOR.join(rows)


def display_board(board):
    print(render_board(board))


def get_available_moves(board):
    return [index for index, value in enumerate(board) if value == EMPTY_CELL]


def is_valid_move(board, move):
    return 0 <= move < len(board) and board[move] == EMPTY_CELL


def apply_move(board, move, marker):
    board[move] = marker


def check_winner(board):
    for a, b, c in WIN_LINES:
        first = board[a]
        second = board[b]
        third = board[c]

        if first == EMPTY_CELL:
            continue

        if first == second == third:
            return first

    return None


def is_draw(board):
    return check_winner(board) is None and not get_available_moves(board)


def board_positions_guide():
    guide = [str(index + 1) for index in range(BOARD_SIZE)]
    return render_board(guide)
