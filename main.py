from game import apply_move, board_positions_guide, check_winner, create_board, display_board, is_draw, is_valid_move


def current_marker(turn_number):
    return "X" if turn_number % 2 == 0 else "O"


def prompt_for_move(board, marker):
    while True:
        raw_value = input(f"Player {marker}, choose a square (1-9): ").strip()

        if not raw_value.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        move = int(raw_value) - 1
        if move < 0 or move > 8:
            print("Please enter a number from 1 to 9.")
            continue

        if not is_valid_move(board, move):
            print("That square is already taken. Try again.")
            continue

        return move


def play_game():
    board = create_board()
    turn_number = 0

    print("Welcome to Tic Tac Toe")
    print()
    print("Board positions:")
    print(board_positions_guide())
    print()

    while True:
        display_board(board)
        print()

        marker = current_marker(turn_number)
        move = prompt_for_move(board, marker)
        apply_move(board, move, marker)

        winner = check_winner(board)
        if winner is not None:
            print()
            display_board(board)
            print()
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print()
            display_board(board)
            print()
            print("It's a draw!")
            break

        turn_number += 1


if __name__ == "__main__":
    play_game()
