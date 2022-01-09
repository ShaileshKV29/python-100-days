from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(20)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
