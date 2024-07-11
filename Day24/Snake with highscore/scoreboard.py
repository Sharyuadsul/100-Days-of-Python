from turtle import Turtle

ALIGNMENT= "center"
FONT = ("arial", 22, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("hscore.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}",align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("hscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center", font=("arial", 22, "normal"))

    def add_score(self):
        self.score += 1
        self.update_score()