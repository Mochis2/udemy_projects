from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.tracer(1)


screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down') 

screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

    
game_on = True
while game_on:
    ball.move()
    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

         
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_horizontal()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_horizontal()
    

    # Detect when either side scored
    if ball.xcor() > 400:
        ball.reset_pos()
        score.left_score()
    

    elif ball.xcor() < -400:
        ball.reset_pos()
        score.right_score()
        

  





screen.exitonclick()