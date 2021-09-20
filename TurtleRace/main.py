from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height = 400)
user_bet = screen.textinput(title= "Make your bet!!",prompt="Wich turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple" ]
cor_y = [-70, -50, -30, -10, 10, 30]
turtle_competidor = []

for turtle in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_turtle.color(colors[turtle])
	new_turtle.goto(x = -280, y = cor_y[turtle])
	turtle_competidor.append(new_turtle)


if user_bet:
	is_race_on = True

while is_race_on:

	for turtle in turtle_competidor:
		if turtle.xcor() > 280:
			is_race_on = False			
			winning_color = turtle.pencolor()
			if user_bet == winning_color:
				print(f"You've Won The {winning_color} is the winner!!")
			else:
				print(f"You've Lost The {winning_color} is the winner!!")

		movement = random.randint(0, 10)
		turtle.forward(movement)


screen.exitonclick()