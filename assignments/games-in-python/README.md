
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game that practices string manipulation, loops, conditionals, and user input handling. The player should guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Build the Hangman game

#### Description
Implement a playable Hangman game in Python. The program should run in the terminal, select a secret word, accept single-letter guesses, and display the current word progress and remaining attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list in the code.
- Prompt the player to guess a single letter each turn and update the displayed progress using underscores for unknown letters (e.g., `_ a _ _ m a n`).
- Track and display letters already guessed and the number of incorrect guesses remaining.
- Prevent repeated guesses from consuming extra attempts.
- End the game when the player either guesses the full word (win) or uses all attempts (lose), and display an appropriate win/lose message including the secret word.
- (Optional) Allow the player to play multiple rounds without restarting the program.

#### Example gameplay

```
Secret word: _ a _ _ m a n
Guessed letters: a
Attempts remaining: 5
Enter a letter: g
Good guess! Secret word: _ a _ _ m a n
```

**Notes:** Keep the implementation simple and well-structured so instructors can run and review it easily.
