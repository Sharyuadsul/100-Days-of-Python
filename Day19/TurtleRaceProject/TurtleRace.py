import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(225)
my_sc = Screen()
my_sc.setup(height=400, width=500)

user_bet = my_sc.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Enter color:").lower()
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
y_pos = [125,75, 25, -25, -75, -125]
all_turtles = []

race_on = False

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for tim in all_turtles:
        if tim.xcor()>220:
            race_on = False
            turtle_color = tim.pencolor()
            if turtle_color == user_bet:
                print(f"You've Won! The {turtle_color} turtle have won the Race")
            else:
                print(f"You've Lost! The {turtle_color} turtle have won the Race")
        else:
            dist = random.randint(0,10)
            tim.forward(dist)






























my_sc.exitonclick()