# Mastermind Colour Match

## Description
Mastermind Colour Match is a terminal-based guessing game where the player must guess a sequence of four colors in the correct order. The game provides feedback on how many colors are correctly placed and how many are misplaced. The player has 10 attempts to solve the puzzle.

## Installation
1. Ensure you have Python installed (Python 3 recommended).
2. Install the required dependencies using:
   ```sh
   pip install colorama
   ```
3. Run the script using:
   ```sh
   python mastermind.py
   ```

## How to Play
- The computer randomly selects four colors from the following list: R (Red), G (Green), B (Blue), Y (Yellow), O (Orange), P (Purple), C (Cyan).
- The player must guess the sequence using the first letter of each color, separated by spaces (e.g., `R G B Y`).
- The game will provide feedback:
  - `Correct Position:` Number of colors guessed in the correct position.
  - `Incorrect Position:` Number of correct colors but in the wrong position.
- The player has **10 attempts** to find the correct sequence.

## Example Gameplay
```
Welcome to Mastermind Colour Match.
You have to guess 4 colours using their first letters separated by spaces.
Here are all the colours used in this game: 'R','G','B','Y','O','P','C'.
You have 10 attempts to guess the correct colours in the correct order.

Enter your guess here (spaces in between): R G B Y
Correct Position: 2 | Incorrect Position: 1
You have 9 attempts left.

Enter your guess here (spaces in between): O P C Y
Correct Position: 1 | Incorrect Position: 2
You have 8 attempts left.
```

## License
This project is under MIT license and free to use.

