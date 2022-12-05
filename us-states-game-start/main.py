from turtle import Turtle, Screen
import pandas


screen = Screen()
s_turtle = Turtle()
screen.title('Us States Quiz')
image = './blank_states_img.gif'
screen.addshape(image)
s_turtle.shape(image)



data = pandas.read_csv('./50_states.csv')
data.state
list_states = list(data.state)

states = Turtle()
states.penup()
states.hideturtle()
score = 0
answers = []
unanswered = []



game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title=f'Guess the State {score}/50', prompt="What's a state's name?").title()
    if answer_state in list(data.state):
        x_coords_state = int(data.loc[data.state == answer_state, 'x'])
        y_coords_state = int(data.loc[data.state == answer_state, 'y'])
        states.goto(x_coords_state-20, y_coords_state)
        states.write(answer_state)
        score += 1
        answers.append(answer_state)

    if answer_state == 'Exit':
        unanswered = [state for state in list_states if state not in answers]
        new_data = pandas.DataFrame(unanswered)
        new_data.to_csv('./states_to_learn.csv')

        break







s_turtle.mainloop()






# screen.exitonclick()