from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

y_pos = -110
for i in range(6):
    tim = Turtle(shape='turtle')
    tim.speed(2)
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=y_pos)
    y_pos += 40
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="Congrats you've won! Now go cry in the corner because i know your life is shit anyways.", prompt='ad')
            else:
                screen.textinput(title='LOSER', prompt="You've lost. Damn you are a loser.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()