from turtle import Turtle


class Borders(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=30)
        self.goto(x,y)

