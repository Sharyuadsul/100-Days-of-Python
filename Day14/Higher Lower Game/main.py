from art import logo
from game_data import data
import random
from art import vs
from replit import clear

print(logo)
print("Welcome to the Higher Lower Game!!")


def extract():
  dict = random.choice(data)
  name = dict["name"]
  description = dict["description"]
  country = dict["country"]
  count = dict["follower_count"]
  return [name, description, country, count]


def game():
  score = 0
  A = extract()
  B = extract()
  if A == B:
    B = extract()
  lost = False
  while not lost:
    while A == B:
      B = extract()
    print(f"Compae A: {A[0]} ,a {A[1]}, from {A[2]}")
    print(vs)
    print(f"against B: {B[0]} ,a {B[1]}, from {B[2]}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    print(logo)
    if guess == 'a':
      if A[3] > B[3]:
        score = score + 1
        print(f"You're Right! Current Score: {score}\n")
        A = B
        B = extract()
      else:
        print(f"You are wrong..You Lost with Score {score}\n")
        lost = True

    elif guess == 'b':
      if B[3] > A[3]:
        score = score + 1
        print(f"You're Right! Current Score: {score}\n")
        A = B
        B = extract()
      else:
        print(f"You are wrong..You Lost with Score {score}\n")
        lost = True


game()
