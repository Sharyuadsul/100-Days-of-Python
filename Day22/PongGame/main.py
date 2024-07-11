from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

my_sc = Screen()
my_sc.setup(height=600, width=800)
my_sc.bgcolor("black")
my_sc.title("PONG")

my_sc.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score = Score()

my_sc.listen()
my_sc.onkey(fun = r_paddle.up, key="Up")
my_sc.onkey(fun = r_paddle.down, key="Down")
my_sc.onkey(fun = l_paddle.up, key="w")
my_sc.onkey(fun = l_paddle.down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    my_sc.update()
    ball.move()
    #collision with the walls(upper and lower)
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()

    #collision with the paddle
    if ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.bounce_x()

    #r paddle missing
    if ball.xcor()>380:
        ball.reset_pos()
        score.l_point()

    #l paddle missing
    if ball.xcor()<-380:
        ball.reset_pos()
        score.r_point()
















my_sc.exitonclick()