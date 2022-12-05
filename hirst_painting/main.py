import turtle as t
import random

tim = t.Turtle()
tim.shape('circle')
tim.resizemode('user')
tim.turtlesize(0.1,0.1,5)
screen = t.Screen()
screen.colormode(255)
tim.pensize(1)
tim.speed(0)

color_list = [(197, 139, 158), (224, 213, 204), (181, 162, 139), (153, 73, 104),
 (180, 94, 128), (151, 177, 185), (233, 199, 205), (129, 102, 58),
 (152, 178, 170), (221, 173, 185), (158, 142, 75), (86, 121, 72), (51, 34, 25),
 (198, 210, 216), (204, 216, 211), (60, 24, 32), (215, 180, 178),
 (202, 196, 170), (114, 37, 57), (99, 81, 14), (109, 144, 95), (166, 110, 101),
 (176, 200, 192), (88, 109, 127), (173, 199, 203), (102, 44, 38),
 (185, 189, 203), (29, 36, 43), (31, 45, 30), (105, 126, 160)]
tim.penup()
tim.setpos(-250, -100)


def dotted_line():
    for i in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    tim.setx(-250)


dotted_line()

def dotted_column():
    for i in range(9):
        tim.color(random.choice(color_list))
        tim.setheading(90)
        tim.forward(50)
        tim.dot(20)


dotted_column()


for i in range(9):
    tim.sety(-100)
    tim.setheading(0)
    tim.forward(50)
    dotted_column()

# 10 by 10 dots 
# each dot size 20
# space between dots 50

































screen.exitonclick()






















# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)