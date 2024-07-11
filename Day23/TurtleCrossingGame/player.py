from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.x_cor= STARTING_POSITION[0]
        self.y_cor= STARTING_POSITION[1]
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)


    def up(self):
        # y_cor = self.ycor()
        # y_cor += 10
        # self.goto(self.xcor(), y_cor)
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(self.x_cor, self.y_cor)

    def finish_line(self):
        if self.ycor()>280:
            return True
        else:
            return False

