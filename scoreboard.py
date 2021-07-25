from turtle import Turtle

FONT = "Courier"
SIZE = 24


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=(FONT, SIZE, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=(FONT, SIZE, "normal"), align="center",)

    def increase_score(self):
        self.score += 1
        self.update_score()