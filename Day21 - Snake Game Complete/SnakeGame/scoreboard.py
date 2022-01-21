from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, align="center",font=('Courier', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center",font=('Courier', 20, 'bold'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.update_scoreboard()