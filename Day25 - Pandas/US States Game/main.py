import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("US States Game/50_states.csv")
states = list(data.state)
guessed_state = []
while len(guessed_state) <= 50:
    answer_state = turtle.textinput(f"{len(guessed_state)}/50 States Correct", "What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states:
        guessed_state.append(answer_state)
        state_data = data[data.state == f"{answer_state}"]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(state_x, state_y)
        state_name.write(f"{answer_state}")

# states_to_learn.csv
not_guessed_states = []
for state in states:
    if state not in guessed_state:
        not_guessed_states.append(state)

states_to_learn = {
    "states": not_guessed_states
}

pandas.DataFrame(states_to_learn).to_csv("US States Game/states_to_learn.csv")