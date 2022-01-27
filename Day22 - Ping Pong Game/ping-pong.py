from turtle import Turtle, Screen
import turtle
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
# screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# screen.tracer(1)
screen.listen()


screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
# print(turtle.tracer())

screen.exitonclick()