from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'
STYLE = 'bold'

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.current_score = 0
        self.color('white')
        self.penup()
        self.goto(position[0],position[1])
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(arg = f'{self.current_score}', move = False, align = ALIGNMENT, font = (FONT, 20, STYLE))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg = 'Game Over', move = False, align = ALIGNMENT, font = (FONT, 16, STYLE))

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write_score()