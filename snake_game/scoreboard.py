from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Fixedsys', 19)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.read_highscore()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.highscore}', align=ALIGNMENT, font=FONT)
        

    def count_score(self):
        self.score += 1
        self.update_score()
    
    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.score = 0
        self.update_score()

    def read_highscore(self):
        with open('udemy_projects/snake_game/data.txt') as data:
            self.highscore = int(data.read())


    def write_highscore(self):
        with open('udemy_projects/snake_game/data.txt', 'w') as write_data:
            write_data.write(str(self.highscore))

        
