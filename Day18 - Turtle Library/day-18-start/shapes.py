from turtle import Turtle, Screen
from random import choice

colors = ["IndianRed1", "LightCyan", "DeepPink", "DarkViolet", "DarkSeaGreen1",
          "CornflowerBlue", "DarkGray", "blue", "red"]
turtle = Turtle()
for sides in range(3, 11):
    turtle.color(choice(colors))
    for draw in range(sides):
        turtle.forward(100)
        turtle.right(360/sides)

# turtle.forward(100)
# turtle.right()


screen = Screen()
screen.exitonclick()