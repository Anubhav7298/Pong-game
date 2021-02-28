from turtle import Screen, Turtle
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)
paddle = Turtle()

paddle_r = Paddle(350)
paddle_l = Paddle(-350)
ball = Ball()
score_r = 0
score_l = 0

screen.listen()
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")
game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce(wall=True)
    if ball.distance(paddle_r.paddle) <= 50 and ball.xcor() > 330:
        ball.bounce(wall=False)
    if ball.distance(paddle_l.paddle) <= 50 and ball.xcor() < -330:
        ball.bounce(wall=False)
    if ball.distance(paddle_r.paddle) > 50 and ball.xcor() > 330:
        ball.reset_position()
        scoreboard.point_l()
    if ball.distance(paddle_l.paddle) > 50 and ball.xcor() < -330:
        ball.reset_position()
        scoreboard.point_r()



screen.exitonclick()
