from turtle import Turtle
import turtle
import random

mycolor = ["red", "green", "purple","yellow","blue","orange"]
speed_increment = 10


class Car_(Turtle):
    def __init__(self,x,y):
        super().__init__()
        #turtle.tracer(0)
        self.color(random.choice(mycolor))
        self.penup()
        self.speed("slowest")
        self.goto(x,y)
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.left(180)
        self.forward(10)
        self.car_speed = speed_increment
        
        #turtle.tracer(1)
    

    def forward_moving(self):
        self.forward(self.car_speed)

    def speed_up(self):
        self.car_speed = speed_increment + 100
      