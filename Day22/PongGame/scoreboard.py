from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.shape("circle")
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", align="center", font=("courier", 24, "normal"))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", align="center", font=("courier", 24, "normal"))

    def l_point(self):
        self.l_score += 1
        self.score_update()

    def r_point(self):
        self.r_score += 1
        self.score_update()