import turtle
import pandas
from States import States

data = pandas.read_csv("50_states.csv")
data_frame = pandas.DataFrame(data)
STATES = data["state"].to_list

print(STATES)

screen = turtle.Screen()
screen.title("U.S states Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state = States()


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name:").capitalize()
for state in STATES:
    if state == answer_state:
        var = data[data_frame["state"] == answer_state]
        state.create_state(var.state, var.x, var.y)


screen.exitonclick()
