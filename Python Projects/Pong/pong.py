import time
from turtle import Turtle, Screen
from paddles import Paddles
from ball import Ball
from borders import Borders
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddles((350,0))
l_paddle = Paddles((-350,0))

left_limit = Borders(0, -300)

ball = Ball()

screen.update()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
ball_y = -5
ball_x = 5
while game_is_on:
    screen.update()
    ball.ball_move(ball_x,ball_y)
    time.sleep(0.1)

    # if ball Hits bottom wall, Y cordiante will change to positive
    if ball.ycor() > 280:
        ball_y = -5

    #if ball Hits bottom wall, Y cordiante will change to positive
    if ball.ycor() < -280:
        ball_y = 5

    #if the ball hits either right or left wall, game over
    if ball.xcor() > 380 or ball.xcor() < -380:
        print("Game is over!")
        game_is_on = False

    #if the ball hits the right paddle, it will go back left
    if ball.distance(r_paddle) < 15:
        ball_x = -5

    #if the ball hits the left paddle, ball will go back right
    if ball.distance(l_paddle) < 15:
        ball_x = +5

screen.exitonclick()