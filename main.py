import turtle
import pandas


screen = turtle.Screen()
screen.setup(500,500)
screen.title("States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
state_x_coords = states.x.to_list()
state_y_coords = states.y.to_list()

guessed_states = []

guess_state = 0
while len(guessed_states) < len(states_list):
    guess = screen.textinput("Guess the State", "Enter a state name (or 'exit' to quit): ").strip().capitalize()
    if guess.lower() == 'exit':
        break
    if guess in states_list and guess not in guessed_states:
        index = states_list.index(guess)
        x = state_x_coords[index]
        y = state_y_coords[index]
        turtle.goto(x, y)
        turtle.write(guess, align='center', font=('Arial', 10, 'normal'))
        guessed_states.append(guess_state)

if len(guessed_states) == len(states_list):
    turtle.goto(0, 250)
    turtle.write("Congratulations! You guessed all states!", align='center', font=('Arial', 20, 'bold'))




    



screen.exitonclick()
