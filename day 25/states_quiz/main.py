import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Create one turtle for writing
t = turtle.Turtle()
t.hideturtle()
t.penup()

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (type 'Exit' to quit)"
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    # Exit condition
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        print("States to learn:", missing_states)
        missed_states=pd.pandas.DataFrame(missing_states)
        missed_states.to_csv("states_to_learn.csv")
        break

    # Correct guess
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()
