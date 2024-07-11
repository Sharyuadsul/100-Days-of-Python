from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

my_sc = Screen()
my_sc.setup(600,600)
my_sc.bgcolor("black")
my_sc.title("Snake Game")
my_sc.tracer(0)

snake = Snake()
food = Food()
score = Score()

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
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.add_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        score.game_over()
    for block in snake.ALL_BLOCKS[1:]:
        if snake.head.distance(block)<10:
            score.game_over()
            game_on = False

my_sc.exitonclick()