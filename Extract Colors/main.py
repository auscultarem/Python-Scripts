import colorgram
from turtle import Turtle, Screen
import random

my_screen =Screen()
my_screen.colormode(255)

tim = Turtle()

rgb_colors = []
colors = colorgram.extract("spots.jpg", 30)

for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	new_color = (r,g,b)
	rgb_colors.append(new_color)


print(rgb_colors)
color_list = [(239, 247, 241), (239, 242, 248), (198, 165, 118), (144, 80, 55), (221, 202, 136), (60, 95, 122), (168, 151, 50), (135, 162, 181), (133, 33, 21), (51, 120, 87), (74, 37, 29), (193, 95, 80), (145, 177, 150), (105, 74, 78), (166, 146, 156), (19, 92, 69), (27, 59, 77), (227, 176, 166), (59, 43, 46), (138, 27, 33), (180, 203, 178), (26, 84, 89), (86, 148, 129), (12, 70, 58), (43, 64, 89), (180, 97, 102), (219, 179, 183), (182, 191, 204)]

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
	tim.dot(20, random.choice(color_list))
	tim.forward(50)
	#make a new line after count 10 dots
	if dot_count %  10 == 0:
		tim.setheading(90)
		tim.forward(50)
		tim.setheading(180)
		tim.forward(500)
		tim.setheading(0)


my_screen.exitonclick()