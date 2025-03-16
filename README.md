# **Mastermind Colour Match Game**

## **Description**
Welcome to the **Mastermind Colour Match Game**! In this game, you will try to guess a sequence of 4 colors chosen by the computer. The colors are represented by their first letters:  
- 'R' = Red  
- 'G' = Green  
- 'B' = Blue  
- 'Y' = Yellow  
- 'O' = Orange  
- 'P' = Purple  
- 'C' = Cyan

The game provides real-time feedback on your guesses and gives you 10 attempts to guess the correct sequence.

---

## **Game Symbols**
The feedback symbols used in the game are:
- `✅` : Correct position and color
- `⚠️` : Correct color, wrong position
- `❌` : Incorrect color

---

## **Gameplay Instructions**
1. The computer randomly selects a sequence of 4 colors.
2. You need to guess the sequence by entering the color initials separated by spaces (e.g., "R G B Y").
3. After each guess, the game provides feedback on the correctness of your guess:
    - `✅` for correctly placed colors.
    - `⚠️` for correct colors in the wrong position.
    - `❌` for incorrect colors.
4. You have **10 attempts** to guess the correct sequence.
5. If you guess correctly, you earn a point and the game congratulates you.
6. If you fail to guess in 10 attempts, the game ends and reveals the correct answer.

---

## **How to Play**
1. Run the Python script to start the game.
2. When prompted, type your guess using the color initials, separated by spaces.
3. After entering your guess, press **Enter** to see the feedback.
4. The game will continue until you guess correctly or run out of attempts.

---

## **Features**
- **Interactive Feedback**: Immediate visual cues for each guess (`✅`, `⚠️`, `❌`).
- **Colorful Interface**: Uses `colorama` for a colorful and engaging terminal experience.
- **Score Tracking**: Keeps track of your score by rewarding you for correct guesses.
- **Game Over Reveal**: Shows the correct sequence at the end if you don’t guess it.

---

## **Requirements**
- Python 3.x
- `colorama` library for color support.

### **Installation of Dependencies**  
To install the `colorama` library, run:
```bash
pip install colorama
```

---

## **Running the Game**
1. Clone the repository or download the Python script.
2. Run the script using:
   ```bash
   python mastermind.py
   ```

3. Follow the instructions in the terminal to play the game.

---

## **Example Run**
```
Welcome to Mastermind Colour Match.
Press ENTER to continue...
You have to guess 4 colours using their first letters separated by spaces.
Press ENTER to continue...
Here are all the colours used in this game: 'R' (Red),'G' (Green),'B' (Blue),'Y' (Yellow),'O' (Orange),'P' (Purple),'C' (Cyan).
Press ENTER to continue...
You have 10 attempts to guess the correct colours in the correct order.
Press ENTER to continue...
Symbols used to represent -
'✅' denotes correct position, '⚠️' correct guess but wrong position, '❌' wrong guess.
```

---

## **Future Improvements**
- Add the ability to play again without restarting the game.
- Improve the game with different difficulty levels (more colors, more positions, etc.).
- Allow users to customize the color choices or the length of the sequence.

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
