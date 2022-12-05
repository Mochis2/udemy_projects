

# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# tommy = Turtle()
# tommy.shape('turtle')
# tommy.color('DarkGoldenrod')
# tommy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = 'l'

print(table)
