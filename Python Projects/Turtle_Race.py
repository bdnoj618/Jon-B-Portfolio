import turtle
from turtle import Turtle, Screen
import random
#racer1 = Turtle(shape="turtle",)
#racer2 = Turtle(shape="turtle")
#racer3 = Turtle(shape="turtle")
#racer4 = Turtle(shape="turtle")
#racer5 = Turtle(shape="turtle")
#
#
#racer1.color("red")
#racer2.color("orange")
#racer3.color("yellow")
#racer4.color("green")
#racer5.color("blue")
#
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which Turtle do you think will win? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
heading = 0

#racer1.penup()
#racer2.penup()
#racer3.penup()
#racer4.penup()
#racer5.penup()
#
#racer1.goto(-230,y=100)
#racer2.goto(-230,y=50)
#racer3.goto(-230,y=0)
#racer4.goto(-230,y=-50)
#racer5.goto(-230,y=-100)

y_postion = [-100, -50, 0, 50, 100]
all_turtles = []
for turtle_index in range(0,5):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postion[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won, the {winning_color} turtle is the Winner.")
            else:
                print(f"You have lost, the {winning_color} turtle is the Winner.")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()