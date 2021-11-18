import time
import turtle
from turtle import Turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_states = []

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Convert the guess to title case
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

def create_turtle(answer_state):
    turtle_two = Turtle()
    turtle_two.hideturtle()
    turtle_two.penup()
    turtle_two.goto(x, y)
    turtle_two.write(answer_state, align='center')
    # all_states.append(turtle_two)
    print(x, y)

# read the csv for states
# Check if the guess is among the 50 states
score = 0
data = pandas.read_csv("50_states.csv")
while answer_state:
    if answer_state == "Exit":
        break
    if (answer_state in data.state.values) and (score < 50):
        coordinates = data[data.state == answer_state]
        x = int(coordinates.x)
        y = int(coordinates.y)
        create_turtle(answer_state)
        all_states.append(answer_state)
        score += 1
    answer_state = screen.textinput(title=f"{score}/50States Correct", prompt="What's another state's name?").title()


# Create data frames
missed_states = []
for i in data.state.values:
    print(i)
    if i not in all_states:
        missed_states.append(i)
df = pandas.DataFrame(missed_states)
df.to_csv('states_to_learn.csv')



