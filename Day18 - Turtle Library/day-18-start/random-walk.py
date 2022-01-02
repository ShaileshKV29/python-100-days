from turtle import Turtle, Screen
from random import choice, random

# colors = ["IndianRed1", "LightCyan", "DeepPink", "DarkViolet", "DarkSeaGreen1",
#           "CornflowerBlue", "DarkGray", "blue", "red"]
turtle = Turtle()
turtle.pensize(10)
turtle.speed('fast')
for walk in range(100):
    penColor_r = random()
    penColor_g = random()
    penColor_b = random()
    turtle.pencolor(penColor_r, penColor_g, penColor_b)
    turtle.forward(30)
    turtle.setheading(choice([0, 90, 180, 270]))

# turtle.forward(100)
# turtle.right()


screen = Screen()
screen.exitonclick()