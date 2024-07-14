#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo

print(logo)
print("Welcome to the Number Guessing Game!!")
import random

num = random.randint(1, 100)
print("I'm Thinking about the number between 1 and 100")
print(f"psst, number guessed is {num}")
difficulty = input(
    "Enter the Difficulty Level that you want..Hard or Easy: ").lower()

if difficulty == "hard":
    turns = 5
else:
    turns = 10


def game(turn):
    win = False
    while turn > 0 and not win:
        print(f"you have {turn} ateempts remaining to guess the number right")
        guess = int(input("Make a Guess: "))
        if guess == num:
            print(f"You Got It! The answer was {num}")
            win = True
        elif guess < num:
            turn = turn - 1
            print("too low")
        else:
            turn = turn - 1
            print("too high")

    if not win:
        print("You run out of guesses. YOU LOSE!")


game(turns)
