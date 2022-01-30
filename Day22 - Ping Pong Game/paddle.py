from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1, 0)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 265:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -265:
            self.goto(self.xcor(), new_y)