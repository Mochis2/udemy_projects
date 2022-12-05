from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray10')
screen.title('Long Dong Silver: THE GAME')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.count_score()
        snake.extend()


    #Detect collsion with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            score.reset_scoreboard()
            snake.reset()

        


    #Detect collision wiht tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset()











screen.exitonclick()