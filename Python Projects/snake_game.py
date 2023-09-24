from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.hideturtle()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")
screen.update()

game_is_on = True
speed = 0.1
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()


    #Detect Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.clear()
        scoreboard.refresh()
        print("nom nom nom")
        if scoreboard.score > 2:
            speed -= 0.01

    #Detect Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Dected Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
