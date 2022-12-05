from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('circle')
tim.color('SlateBlue4')
tim.resizemode('user')
tim.turtlesize(0.1,0.1,5)
tim.pensize(1)
tim.speed(0)
screen = Screen()
# screen.bgcolor('MediumPurple3')
screen.colormode(255)

# ----draw dotted line----
# tim.penup()
# tim.setpos(-500, 0)
# for line in range(100):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


# ----draw triangle until decagon----
colors = ['PapayaWhip','PeachPuff','PeachPuff1','PeachPuff2','PeachPuff3','PeachPuff4','LightSkyBlue1','LightSkyBlue2','LightSkyBlue','LightSkyBlue3','LightSkyBlue4','LightSlateBlue','LightYellow','LightYellow1','LightYellow2']  
# i = 0
# num_of_sides = 3
# while num_of_sides <= 10:
#     for line in range(num_of_sides):
#         tim.forward(100)
#         tim.right(360/num_of_sides)
#     tim.color(colors[i])
#     i += 1
#     num_of_sides += 1


# ----my solution to random drawing in all four directions :(----
    
# directions = [1,2,3,4]
# length = 15
# def forward():
#     tim.forward(length)
    
# def backward():
#     tim.back(length)
    
# def right():
#     tim.right(90)
#     tim.forward(length)

# def left():
#     tim.left(90)
#     tim.forward(length)
    
# def color_choice():
#     tim.color(random.choice(colors))

# def which_direction():
#     where_to_go = random.choice(directions)
#     if where_to_go == 1:
#         return forward(), color_choice()
#     elif where_to_go == 2:
#         return backward(), color_choice()
#     elif where_to_go == 3:
#         return right(), color_choice()
#     elif where_to_go == 4:
#         return left(), color_choice()

# is_on = True
# while is_on:
#     which_direction()


# ----the solution for random drawing in all four directions----
def random_colours():
    color_1 = random.choice(range(255))
    color_2 = random.choice(range(255))
    color_3 = random.choice(range(255))
    color_tuple = (color_1, color_2, color_3)
    return color_tuple

# directions = [0, 90, 180, 270]
# for _ in range(300):
#     color_1 = random.choice(range(255))
#     color_2 = random.choice(range(255))
#     color_3 = random.choice(range(255))
#     tim.color(color_1, color_2, color_3)
#     tim.forward(20)
#     tim.setheading(random.choice(directions))

number = 5
size_of_gap = number
for i in range(int(360/size_of_gap)):
    tim.color(random_colours())
    tim.circle(100)
    tim.setheading(size_of_gap)
    size_of_gap += number










screen.exitonclick()