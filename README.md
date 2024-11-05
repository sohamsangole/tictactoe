# Pygame Tic Tac Two

A simple implementation of the classic Tic Tac Toe game using Pygame. This game features a graphical interface where two players can take turns placing X's and O's on a 3x3 grid.

## Requirements

- Pygame library

## Installation

1. Install Pygame using pip:
```bash
pip install pygame
```
2. Download the game file and save it as `tictactoe.py`

## How to Play

1. Run the game:
```bash
python tictactoe.py
```

2. Game Rules:
   - Players take turns clicking on empty squares
   - Player X goes first (black X)
   - Player O goes second (black circle)
   - If all squares are filled with no winner, the game is a draw

3. Controls:
   - Click an empty square to place your mark
   - Close the window to exit the game

### Key Functions

- `drawBoard()`: Creates the game grid
- `drawX()`: Draws X marks
- `drawO()`: Draws O marks
- `getPosi()`: Converts mouse clicks to grid positions
- `winstate()`: Checks for winning conditions
- `drawstate()`: Checks for draw conditions
- `printBoard()`: Displays current game state in console

## Termination

The game ends when either:
- A player wins (three in a row)
- The board is full (draw)
- The window is closed

Game results are displayed in the console before the program exits.

## License

This project is open source and available for educational and personal use.