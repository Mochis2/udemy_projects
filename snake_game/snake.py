from turtle import Turtle, Screen


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (0, -20), (0, -40)]


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]


    def create_snake(self):
        '''creates the starting snake'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle(shape='square')
        new_snake.speed(0)
        new_snake.penup()
        new_snake.color('white')
        new_snake.goto(position)
        self.snake_segments.append(new_snake)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]



    def move(self):
        '''Moves the snake by 20'''
        for seg_num in range(len(self.snake_segments)-1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        '''When pressing "Up" the snake goes up'''
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        '''When pressing "Down" the snake goes down'''
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        '''When pressing "Left" the snake goes left'''
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        '''When pressing "Right" the snake goes right'''
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)