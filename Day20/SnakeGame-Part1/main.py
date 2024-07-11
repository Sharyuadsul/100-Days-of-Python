from turtle import Turtle, Screen
import time
from snake import Snake

my_sc = Screen()
my_sc.setup(600,600)
my_sc.bgcolor("black")
my_sc.title("Snake Game")
my_sc.tracer(0)

snake = Snake()

my_sc.listen()
my_sc.onkey(fun=snake.up, key="Up")
my_sc.onkey(fun=snake.down, key="Down")
my_sc.onkey(fun=snake.left, key="Left")
my_sc.onkey(fun=snake.right, key="Right")


game_on = True

while game_on:
    my_sc.update()
    time.sleep(0.1)
    snake.move()


































my_sc.exitonclick()