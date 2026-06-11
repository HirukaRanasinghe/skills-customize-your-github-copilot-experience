# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game in Python. You will practice strings, loops, conditionals, random selection, and user input while creating a game that reveals a hidden word one letter at a time.

## 📝 Tasks

### 🛠️ Set Up the Secret Word

#### Description
Create the data needed for the game and choose a hidden word for the player to guess.

#### Requirements
Completed program should:

- Store a predefined list of possible words in the program.
- Randomly select one word at the start of the game.
- Display the word as a hidden pattern using underscores, such as `_ _ _ _`.

### 🛠️ Handle Letter Guesses

#### Description
Build the main game loop so the player can guess one letter at a time and see their progress.

#### Requirements
Completed program should:

- Ask the player to enter a single letter guess.
- Reveal the correct letters in the hidden word when the guess is correct.
- Keep track of letters that have already been guessed.
- Show the current progress after each guess.

### 🛠️ Finish the Game

#### Description
Add win and lose conditions so the game ends when the player solves the word or runs out of attempts.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining.
- End the game when the player guesses the full word.
- End the game when the player runs out of attempts.
- Display a clear win or lose message at the end of the game.
