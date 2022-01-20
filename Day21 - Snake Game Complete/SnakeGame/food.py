import turtle
import random

from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-480, 480)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x, self.random_y)
