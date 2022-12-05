from turtle import Turtle,Screen

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def update_score(self):
        Screen().tracer(0)
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align='center', font=('Fixedsys', 30))
        self.goto(100, 250)
        self.write(self.r_score, align='center', font=('Fixedsys', 30))
        Screen().tracer(1)



    def right_score(self):
        self.r_score += 1
        self.update_score()        


    def left_score(self):
        self.l_score += 1
        self.update_score()        
