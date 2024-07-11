import colorgram
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
# colors = colorgram.extract("spot.jpg",30)
# #print(colors)
#
#
# color = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color.append((r,g,b))
#
# print(color)

colors = [(178, 12, 36), (229, 244, 237), (182, 76, 26),
          (213, 158, 78), (245, 214, 75), (178, 172, 16), (173, 22, 15), (118, 183, 202),
          (220, 130, 160), (61, 50, 107), (53, 97, 156), (66, 36, 59), (159, 53, 75),
          (37, 135, 90), (35, 53, 69), (103, 188, 161), (218, 72, 131), (78, 46, 38), (237, 203, 2),
          (21, 167, 149), (53, 172, 187), (150, 211, 221), (161, 183, 229), (44, 62, 61), (233, 166, 182),
          (80, 104, 184)]

dots = 100
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(350)
timmy.setheading(0)


for i in range(1,dots+1):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)

    if i%10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_sc = t.Screen()
my_sc.exitonclick()