import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
#from scoreboard import Scoreboard

EASY = 10
MEDIUM = 15
HARD = 20
cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

timmy = Player()
for select_car in range(EASY):
    car = CarManager()
    cars.append(car)



screen.listen()
screen.onkey(timmy.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    a = random.choice(cars)
    a.move()






screen.exitonclick()