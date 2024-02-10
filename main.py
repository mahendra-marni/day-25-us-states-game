import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S STATES QUIZ")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
answer_states = data.state.to_list()
guessed_states = []
t = turtle.Turtle()
t.hideturtle()
t.penup()
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="Enter the state name").title()
    var = data[data["state"] == answer]
    if answer == "Exit":
        states_to_learn = []
        for state_name in answer_states:
            if state_name in guessed_states:
                continue
            else:
                states_to_learn.append(state_name)

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn")
        break

    if answer in answer_states:
        t.goto(x=int(var.x), y=int(var.y))
        t.write(f"{answer}")
        guessed_states.append(answer)
