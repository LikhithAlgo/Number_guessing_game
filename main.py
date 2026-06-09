import random

LOW = 1
HIGH = 100

answer = random.randint(LOW, HIGH)
guesses = 0

print("\n===== WELCOME TO THE NUMBER GUESSING GAME =====")
print(f"Guess a number between {LOW} and {HIGH}")

while True:
    guess = input("\nEnter your guess: ")

    # Check if input is a number
    if not guess.isdigit():
        print("❌ Invalid input! Please enter a number.")
        continue

    guess = int(guess)
    guesses += 1

    # Check range
    if guess < LOW or guess > HIGH:
        print(f"❌ Please enter a number between {LOW} and {HIGH}.")
        continue

    # Compare guess with answer
    if guess < answer:
        print("📉 Too low! Try again.")
    elif guess > answer:
        print("📈 Too high! Try again.")
    else:
        print("\n🎉 Congratulations!")
        print(f"You guessed the correct number: {answer}")
        print(f"Total guesses: {guesses}")
        break