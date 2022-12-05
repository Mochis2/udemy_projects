from turtle import Turtle,Screen

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.write_level_score()
    
    def write_game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=FONT)

    def write_level_score(self):
        self.penup()
        self.clear()
        self.goto(-280, 260)
        self.write(f'Level: {self.score}', align='left', font=FONT)

    
    def increase_level(self):
        self.score += 1
        self.write_level_score()
