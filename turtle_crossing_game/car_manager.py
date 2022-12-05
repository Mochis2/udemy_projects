from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:

    

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed_increase = 0


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.goto(320, random.randint(-250,250))
            self.all_cars.append(car)
        
    
    
    def move_cars_faster(self):
        self.speed_increase += MOVE_INCREMENT
        self.move_cars()
    

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE + self.speed_increase)
       





    
