import turtle as t

timmy = t.Turtle(shape="turtle")

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_left():
    curr_head = timmy.heading()
    timmy.setheading(curr_head + 10)

def turn_right():
    curr_head = timmy.heading()
    timmy.setheading((curr_head-10))

my_sc = t.Screen()
my_sc.listen()
my_sc.onkey(fun= move_forward, key="w")
my_sc.onkey(fun=move_backward, key="s")
my_sc.onkey(fun=turn_left, key="a")
my_sc.onkey(fun=turn_right, key="d")





my_sc.exitonclick()