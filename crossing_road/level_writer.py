import turtle
from turtle import Turtle


class ScoreWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        #turtle.color("")

    def level(self, level_):
        self.goto(-240, 170)
        self.clear()
        self.write(f'Level: {level_}', move= False, font=("Arial", 20, "normal"))
        self.hideturtle()
        
    
    def game_over(self):
        #turtle.clear()
        self.goto(-50, 0)
        self.write(f'GAME OVER', move= False, font=("Arial", 20, "normal"))
        self.hideturtle()