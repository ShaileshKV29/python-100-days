from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(1, 5, 0)
paddle.setheading(90)
paddle.penup()
paddle.goto(350, 0)
screen.listen()
# paddle.left(20)

def move_up():
    paddle.forward(20)

def move_down():
    paddle.backward(20)

screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

screen.exitonclick()