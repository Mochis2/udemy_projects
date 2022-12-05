from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600,height=600)
turtle = Turtle()
turtle.penup()
turtle.ht()
turtle.goto(-40,260)
# turtle.shearfactor(-0.5)
turtle.write("Home = ", move=True, font=('Fixedsys', 20))


screen.exitonclick()


class Test(Turtle):

    def __init__(self):
        super().__init__()