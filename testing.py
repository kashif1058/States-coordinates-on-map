import turtle
import pandas as pd

# Initialize turtle screen
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("States Guessing Game")

# Load and display map image
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

# Load state data
states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()

# Initialize variables
guessed_states = []
score = 0

# Function to handle clicking on state
def state_clicked(x, y):
    global score
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(state_name, align='center', font=('Arial', 10, 'normal'))
    score += 1
    guessed_states.append(state_name)
    if score == len(states_list):
        turtle.goto(0, 250)
        turtle.write("You guessed all states!", align='center', font=('Arial', 20, 'bold'))

# Listen for clicks on the map
turtle.onscreenclick(state_clicked)

# Main game loop
while len(guessed_states) < len(states_list):
    state_name = screen.textinput(f"Guess the State ({score}/{len(states_list)})", "Enter a state name: ").title()

    if state_name == "Exit":
        break

    if state_name in states_list and state_name not in guessed_states:
        state_data = states_data[states_data['state'] == state_name].iloc[0]
        x = float(state_data['x'])
        y = float(state_data['y'])
        turtle.goto(x, y)
        turtle.write(state_name, align='center', font=('Arial', 10, 'normal'))
        score += 1
        guessed_states.append(state_name)

# End game message
if len(guessed_states) == len(states_list):
    turtle.goto(0, 250)
    turtle.write("Congratulations! You guessed all states!", align='center', font=('Arial', 20, 'bold'))

# Keep the window open until the user closes it
turtle.mainloop()