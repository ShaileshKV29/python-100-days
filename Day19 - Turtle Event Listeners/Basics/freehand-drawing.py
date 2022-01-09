from turtle import Turtle, Screen


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.forward(-10)


def turn_clockwise():
    turtle.right(15)


def turn_anti_clockwise():
    turtle.left(15)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle = Turtle()
screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_anti_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
