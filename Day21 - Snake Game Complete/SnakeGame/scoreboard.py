from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", True, align="center",font=('Meryweather', 16, 'normal'))
        self.speed("fastest")
        self.sety(290)

    def add_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", True, align="center",font=('Meryweather', 16, 'normal'))