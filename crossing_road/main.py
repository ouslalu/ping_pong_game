from tkinter import N
from turtle import Turtle, Screen
import random
from player import Crosser
from car import Car_
from level_writer import ScoreWriter
#import numpy
import turtle 
import time



screen = Screen()
screen.setup(width= 500, height= 400)
screen.bgcolor("white")
screen.title("Crossing Road")

crosser = Crosser()
scorewriter = ScoreWriter()
#car = Car_(100,100)


screen.listen()
screen.onkey(crosser.move, "Up")
speed = 0.1
#crosser = Crosser()
car_list = []
turtle.tracer(0)
for i in range(20):
        car = Car_(random.randrange(-240,240,10), random.randrange(-140,150,25))
        car_list.append(car)
#turtle.tracer(1)
backward_list = []
for i in range(2000):
    car = Car_(random.randrange(220,100000,10), random.randrange(-140,150,25))
    backward_list.append(car)
#def trailing_cars():
    # for back_car in backward_list:
    #     back_car.forward_moving()
#crosser.move()
level_ = 1
scorewriter.level(level_)
keep_moving = True
while keep_moving:
    for car in car_list:
        car.forward_moving()
        print(crosser.distance(car))
        if car.distance(crosser) < 18:
            scorewriter.game_over()
            keep_moving = False
    for back_car in backward_list:
        back_car.forward_moving()
        if back_car.distance(crosser) < 18:
            scorewriter.game_over()
            keep_moving = False
    if crosser.ycor() > 180:
        crosser.goto(0, -180)
        level_ = level_+1
        scorewriter.level(level_)
        car.speed_up()
    time.sleep(0.1)
    #print(speed)
    screen.update()

with open("21/ping_pong_game/crossing_road/score_card.txt", "w") as f:
    f.write(str(level_)) 
f.close()




screen.exitonclick()
