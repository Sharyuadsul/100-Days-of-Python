rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer= random.randint(0,2)
if user == 0:
  if computer == 0:
    print(f"your choice: Rock \n{rock} \n Computer's Choice: Rock \n{rock}\n Tie!!")
  elif computer == 1:
    print(f"your choice: Rock \n{rock} \n Computer's Choice: paper \n{paper}\n You Lost!!")
  else:
    print(f"your choice: Rock \n{rock} \n Computer's Choice: scissors\n{scissors}\n You Won!!")
elif user == 1:
  if computer == 0:
    print(f"your choice: Paper \n{paper} \n Computer's Choice: Rock \n{rock}\n You Won!!")
  elif computer == 1:
    print(f"your choice: Paper \n{paper} \n Computer's Choice: paper \n{paper}\n Tie!!")
  else:
    print(f"your choice: Paper \n{paper} \n Computer's Choice: scissors\n {scissors}\n You Lost!!")
else:
  if computer == 0:
    print(f"your choice: Scissor \n{scissors} \n Computer's Choice: Rock \n {rock}\n You Lost!!")
  elif computer == 1:
    print(f"your choice: Scissor \n{scissors} \n Computer's Choice: paper \n{paper}\n You Won!!")
  else:
    print(f"your choice: Scissor \n{scissors} \n Computer's Choice: scissors\n{scissors}\n Tie!!")