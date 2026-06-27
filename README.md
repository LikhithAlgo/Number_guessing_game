# Number Guessing Game

A simple command-line number guessing game built with Python, where the player tries to guess a randomly generated number within a set range.

## Features
- Randomly generates a number between 1 and 100
- Validates input (rejects non-numeric and out-of-range guesses)
- Gives feedback after each guess ("too low" / "too high")
- Tracks and displays total number of guesses once the correct number is found

## Tech Stack
- Python (no external libraries required)
- `random` module for generating the target number

## How to Run
1. Make sure you have Python installed
2. Run: `python main.py`

## How It Works
- The game picks a secret number between 1 and 100
- You keep guessing until you find it
- Each guess is checked:
  - Must be a valid number
  - Must be within the 1–100 range
  - Compared against the secret number for "too low" / "too high" feedback
- Once guessed correctly, your total number of attempts is shown

## Future Improvements
- Add difficulty levels (different number ranges or limited guess attempts)
- Add a play-again option without restarting the script
- Track and display best score (fewest guesses) across multiple rounds

