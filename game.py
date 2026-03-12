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
    formatted_rows = []

    for row_index in range(ROW_SIZE):
        # Convert the flat board into visual rows of 3 cells each.
        row_start = row_index * ROW_SIZE
        row_cells = board[row_start:row_start + ROW_SIZE]

        # Turn something like ["X", "O", " "] into "X | O |  ".
        formatted_row = " | ".join(row_cells)
        formatted_rows.append(f" {formatted_row} ")

    # Join the 3 rendered rows with a horizontal separator.
    return ROW_SEPARATOR.join(formatted_rows)


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
        # Look up the 3 cells that make up one possible winning line.
        first = board[a]
        second = board[b]
        third = board[c]

        # An empty line cannot be a winning line.
        if first == EMPTY_CELL:
            continue

        # If all 3 cells match, return the winning marker.
        if first == second == third:
            return first

    return None


def is_draw(board):
    return check_winner(board) is None and not get_available_moves(board)


def board_positions_guide():
    # Build a reference board so players can see how numbers map to squares.
    guide = [str(index + 1) for index in range(BOARD_SIZE)]
    return render_board(guide)
