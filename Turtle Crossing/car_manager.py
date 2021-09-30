import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LENGHT = 1
WIDTH = 2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color_car = random.choice(COLORS)
        self.x_pos = 270
        self.y_pos = 0
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid = LENGHT, stretch_len = WIDTH)
        self.penup()
        self.color(self.color_car)
        self.y_pos = random.randint(-270, 270)
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto( new_x, self.ycor())