from turtle import Turtle


class Paddle:
    def __init__(self, pos):
        self.paddle = Turtle()
        self.pos = pos
        self.create_paddle()

    def create_paddle(self):
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.up()
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.setpos(self.pos, 0)

    def move_up(self):
        if self.paddle.ycor() < 230:
            c = self.paddle.ycor() + 20
            self.paddle.goto(self.paddle.xcor(), c)

    def move_down(self):
        if self.paddle.ycor() > -230:
            c = self.paddle.ycor() - 20
            self.paddle.goto(self.paddle.xcor(), c)