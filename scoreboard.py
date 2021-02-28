from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.score_l = 0
        self.score_r = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Arial", 28, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Arial", 28, "normal"))

    def point_l(self):
        self.score_l += 1
        self.update()

    def point_r(self):
        self.score_r += 1
        self.update()
