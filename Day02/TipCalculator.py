#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator")
print("What was the total bill?")
bill = float(input())
print("How much tip would you like to give? 10, 12, or 15% ?")
tip = int(input())
print("How many people to split the Bill?")
people = int(input())
payment = round(((bill + ((tip / 100) * bill)) / people), 2)
#payment = "{:.2f}".format((bill + ((tip / 100) * bill)) / people)
print(f"Each person should pay: ${payment}. ")