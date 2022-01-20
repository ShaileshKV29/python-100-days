from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Snake Game")
screen.listen()
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    

screen.exitonclick()
