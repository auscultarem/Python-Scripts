# import pandas
from turtle import Turtle
# data = pandas.read_csv("50_states.csv")
# print(data_frame)
# var = data[data_frame["state"] == "Alabama"] # I can access to the row element
# print(var)
# print(var.x) # I can access to the attribute x
# print(var.y) # I can access to the attribute y

class States:
    def __init__(self):
        self.us_states = []

    def create_state(self, name, xcor, ycor):
            new_state = Turtle('turtle')
            new_state.penup()
            new_state.name = name
            new_state.goto(xcor, ycor)
            self.us_states.append(new_state)