from turtle import Turtle

ANGLES = [45]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(1)
        self.penup()

    def ball_move(self,x , y):
        new_x = self.xcor() + x
        new_y = self.ycor() + y
        self.goto(new_x, new_y)


    def ball_bounce(self):
        new_x = self.xcor() + 5
        new_y = self.ycor() - 5
        self.goto(new_x, new_y)
