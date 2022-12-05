import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    
  
    # Creates and moves cars
    car.create_car()
    car.move_cars()

    # Detect collision with the cars
    for cars in car.all_cars:
        distance_to_cars = cars.distance(player)
        if distance_to_cars < 20:
            score.write_game_over()
            game_is_on = False

    # If player crossed the street turtle resets, speed and level increases
    if player.if_finished_reset_position():
        car.move_cars_faster()
        score.increase_level()
        
        




    

    









screen.exitonclick()



# 1 turtle needs to move to the top of the screen
## Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. 
## If you get stuck, check the video walkthrough in Step 3.

# 2 turtle needs to reset after top of the screen is reached
## Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
## No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
## Hint: generate a new car only every 6th time the game loop runs. 
## If you get stuck, check the video walkthrough in Step 4.

# 3 cars need to go from left to right
## Detect when the turtle player collides with a car and stop the game if this happens. 
## If you get stuck, check the video walkthrough in Step 5.

# 4 more cars and random
## Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
## When this happens, return the turtle to the starting position and increase the speed of the cars. 
## Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. 
## If you get stuck, check the video walkthrough in Step 6.

# 5 collision with cars if so game over

# 6 score and level diff needs to increase after reaching end
## Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. 
## When the turtle hits a car, GAME OVER should be displayed in the centre. 
## If you get stuck, check the video walkthrough in Step 7.