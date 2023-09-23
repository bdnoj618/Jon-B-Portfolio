import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(1)
turtle.colormode(255)
angle = 0
direction = [0, 90, 180, 270]
color = ["DarkOrange", "blue", "DarkRed", "aquamarine", "black", "brown"]

def random_Direction():
    #direct = random.choice(direction)
    tim.setheading(angle)


def random_color():

    tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))


tim.speed(0)

for _ in range(100):
    random_Direction()
    #tim.forward(25)
    random_color()
    tim.circle(100)
    angle += 9

screen = Screen()
screen.exitonclick()
