from turtle import Turtle

WIDTH = 1
LENGTH = 5
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # Each saqre has 20 pixels
        self.shapesize(stretch_wid=LENGTH,
                       stretch_len=WIDTH)  # 20 pixel plus 5 = 100 length, 20 pixel plus 1 = 20 width
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
