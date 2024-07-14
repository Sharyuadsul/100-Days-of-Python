from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bidding_record = {}


def highest_bid():
  highest = 0

  for key in bidding_record:
    if bidding_record[key] > highest:
      highest = bidding_record[key]
      winner = key
  print(f"winner of the bidding is {winner} with highest bid of {highest}")


bidding_finished = False

while not bidding_finished:
  name = input("Enter the name: ")
  bid = int(input("Enter your bid: "))
  bidding_record[name] = bid
  bidding_continue = input(
      "Are there any more bidders? Type 'yes' or 'no' ").lower()
  if bidding_continue == "yes":
    clear()
  elif bidding_continue == "no":
    highest_bid()
    bidding_finished = True
