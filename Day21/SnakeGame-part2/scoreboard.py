from turtle import Turtle

ALIGNMENT= "center"
FONT = ("arial", 22, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=("arial", 22, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()