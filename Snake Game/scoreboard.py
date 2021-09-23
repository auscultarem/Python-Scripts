from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.penup()
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGMENT, font=FONT)

    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        self.hideturtle()
