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

# print(snake.xcor())

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()
    
    if snake.xcor() < -500 or snake.xcor() > 480:
        game_is_on = False

    if snake.ycor() < -280 or snake.ycor() > 280:
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

score.game_over()
    

screen.exitonclick()
