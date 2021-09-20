from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.speed("fastest")

def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	random_choice = (r, g, b)
	return random_choice

for angle in range(1, 360):
	timmy.pencolor(random_color())
	timmy.circle(100)
	timmy.right(angle)
	