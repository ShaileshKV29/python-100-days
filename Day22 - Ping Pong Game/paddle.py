from turtle import Turtle
from venv import create

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self = Turtle("square")
        self.color("white")
        self.shapesize(5, 1, 0)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        print(self.xcor())

    def move_down(self):
        print("Move Down")
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)