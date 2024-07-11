from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.ALL_BLOCKS = []
        self.create_snake()
        self.head = self.ALL_BLOCKS[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_block(i)

    def reset(self):
        for seg in self.ALL_BLOCKS:
            seg.goto(1000,1000)
        self.ALL_BLOCKS.clear()
        self.create_snake()
        self.head = self.ALL_BLOCKS[0]


    def add_block(self,position):
        timmy = Turtle()
        timmy.shape("square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.ALL_BLOCKS.append(timmy)

    def extend(self):
        self.add_block(self.ALL_BLOCKS[-1].position())

    def move(self):
        for block in range(len(self.ALL_BLOCKS)-1, 0, -1):
            new_x = self.ALL_BLOCKS[block - 1].xcor()
            new_y = self.ALL_BLOCKS[block - 1].ycor()
            self.ALL_BLOCKS[block].goto(new_x, new_y)

        self.ALL_BLOCKS[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.ALL_BLOCKS[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.ALL_BLOCKS[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.ALL_BLOCKS[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.ALL_BLOCKS[0].setheading(0)
