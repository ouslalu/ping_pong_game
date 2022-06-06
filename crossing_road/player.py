import turtle
from turtle import Turtle


class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        turtle.tracer(0)
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.goto(0, -175)
        self.shapesize(0.8)
        self.left(90)
        #self.forward(10)
        turtle.tracer(1)

    
    def move(self):
        self.forward(10)