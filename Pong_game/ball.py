from turtle import Turtle, Screen
import time

SPEED = 2
SPEED_MULITPLIER = 0.1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = SPEED
        self.y_move = SPEED
        self.move_speed = SPEED_MULITPLIER

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.y_move *= -1

    def bounce_horizontal(self):
        self.x_move *= -1
        self.x_move += self.move_speed * self.x_move
        self.y_move += self.move_speed * self.y_move

    # def test(self):
        # Screen().tracer(1)


    def reset_pos(self):
        Screen().tracer(0)
        self.home()
        self.x_move = SPEED
        self.y_move = SPEED
        time.sleep(1)
        Screen().onkeypress(self.home, 'space')
