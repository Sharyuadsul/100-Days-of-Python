#from turtle import Turtle, Screen
import random
import turtle

timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("blue2")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     #or you can also change the pencolor()
#     timmy.forward(10)
#     timmy.pendown()


# angle = 360
# parts = 3
# colors =["spring green", "aquamarine", "medium blue", "peru", "hot pink", "orange", "yellow"]
# for _ in range(8):
#     theta = angle/parts
#     timmy.color(random.choice(colors))
#     for i in range(parts):
#         timmy.forward(100)
#         timmy.right(theta)
#     parts += 1


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
# for shape_side_n in range(3, 10):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)


turtle.colormode(255)
# def random_col():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)
#
# timmy.pensize(5)
# sides = [0,90,180.270]
# timmy.speed("fastest")
# for i in range(100):
#     timmy.color(random_col())
#     timmy.forward(30)
#     timmy.setheading(random.choice(sides))

def random_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

timmy.speed("fastest")
def spiral(size):
    for i in range(int(360/size)):
        timmy.color(random_col())
        timmy.circle(100)
        timmy_head = timmy.heading()
        timmy.setheading(timmy_head + size)

spiral(5)




































my_sc = Screen()
my_sc.exitonclick()
