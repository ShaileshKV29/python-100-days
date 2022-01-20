from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Snake Game")
screen.listen()
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
    

screen.exitonclick()
