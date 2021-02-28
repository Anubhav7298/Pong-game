from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.up()
        self.speed = 0.2
        self.x_move = self.speed
        self.y_move = self.speed

    def move(self):

        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce(self, wall):
        if wall:
            self.y_move *= -1
        else:
            self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce(wall=False)