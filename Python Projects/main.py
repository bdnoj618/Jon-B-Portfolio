#import turtle
#
#import colorgram
#
#colors = colorgram.extract('Dots.jpg',30)
#
#rgb_colors = []
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)
#Dots 20 size spaced out by 50
#10x10 array of dots
import turtle
from turtle import Turtle, Screen
import random


def Random_Color():
    return(random.choice(color))


color = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]
tim = Turtle()
turtle.colormode(255)
right = True
heading = 90
tim.penup()
tim.setpos(-300,-300 )
for n in range(10):
    if not right:
        heading = 180
    elif right:
        heading = 0
    for i in range(10):
        tim.dot(20,Random_Color())
        tim.setheading(heading)
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    if not right:
        right = True
        tim.setheading(0)
        tim.forward(50)
    else:
        right = False
        tim.setheading(180)
        tim.forward(50)
screen = Screen()
screen.exitonclick()