from game import (
    apply_move,
    board_positions_guide,
    check_winner,
    create_board,
    display_board,
    is_draw,
    is_valid_move,
)

VALID_RANGE_MESSAGE = "Please enter a number from 1 to 9."


def show_intro():
    print("Welcome to Tic Tac Toe")
    print()
    print("Board positions:")
    print(board_positions_guide())
    print()
    print("Player 1 is X.")
    print("Player 2 is O.")
    print("X goes first.")
    print()


def parse_move(raw_value):
    if not raw_value.isdigit():
        return None

    move = int(raw_value) - 1
    if move < 0 or move > 8:
        return None

    return move


def prompt_for_move(board, prompt):
    while True:
        raw_value = input(prompt).strip()

        move = parse_move(raw_value)
        if move is None:
            print(VALID_RANGE_MESSAGE)
            continue

        if not is_valid_move(board, move):
            print("That square is already taken. Try again.")
            continue

        return move


def finish_game(board, message):
    print()
    display_board(board)
    print()
    print(message)


def play_game():
    board = create_board()

    show_intro()
    current_player = 1

    while True:
        display_board(board)
        print()

        if current_player == 1:
            marker = "X"
        else:
            marker = "O"

        prompt = f"Player {current_player} ({marker}), choose a square (1-9): "

        move = prompt_for_move(board, prompt)

        apply_move(board, move, marker)

        winner = check_winner(board)
        if winner is not None:
            finish_game(board, f"Player {current_player} ({marker}) wins!")
            break

        if is_draw(board):
            finish_game(board, "It's a draw!")
            break

        current_player = 2 if current_player == 1 else 1


if __name__ == "__main__":
    play_game()
