# Recurse Center Pairing Interview - Tic Tac Toe

Terminal Tic Tac Toe written in Python.

Initial version scaffolded with GPT-5.4, then reviewed and prepared for live explanation and extension during the interview.

## Goal

Build a clean two-player terminal game that is easy to explain and easy to extend live during the pairing interview.

## Before The Interview

The initial version should support:

- Two human players taking turns
- Input validation
- Board rendering in the terminal
- Win detection
- Draw detection
- Clean restart by rerunning the script

## Pairing Interview Plan

During the pairing interview, add a computer player.

## Pseudocode-Driven Development

The goal is to explain the design first, then implement it in small steps.

Current game flow:

```text
start game
create empty board
show intro and board positions
set Player 1 to X
set Player 2 to O
set current player to 1

repeat until game ends:
    display board
    ask the current player for a move
    validate the input

    place marker on board

    if someone won:
        end game

    if the board is full:
        end game as draw

    switch current player
```

Win detection logic:

```text
winning lines =
    top row:    (0, 1, 2)
    middle row: (3, 4, 5)
    bottom row: (6, 7, 8)
    left col:   (0, 3, 6)
    mid col:    (1, 4, 7)
    right col:  (2, 5, 8)
    diagonal:   (0, 4, 8)
    diagonal:   (2, 4, 6)

for each winning line (a, b, c):
    if board[a] is empty:
        continue

    if board[a] == board[b] == board[c]:
        return that marker

return no winner
```

Draw detection logic:

```text
if there is no winner and there are no empty squares left:
    return draw
else:
    game continues
```

Note:

- The code tracks turns with player numbers (`1` and `2`). Player 1 is always `X`, Player 2 is always `O`, and Player 1 goes first. This keeps the flow easy to explain.

Planned interview extension:

```text
for each turn:
    display board

    if current player is human:
        prompt for move
    else:
        choose a valid computer move

    apply move

    if someone won:
        end game

    if board is full:
        end game as draw
```

Suggested order:

1. Let Player 2 become a computer player.
2. Implement a simple random move generator for `O`.
3. If time remains, improve the computer player to:
   - take a winning move
   - block an opponent's winning move

## How To Run

```bash
python3 main.py
```

## Suggested Submission Note

Terminal Tic Tac Toe written in Python. During the pairing interview, I'd like to add a computer player, starting with random valid moves and improving the strategy if time allows.
