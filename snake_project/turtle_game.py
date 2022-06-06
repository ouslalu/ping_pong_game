
from turtle import Turtle, Screen, tracer
import turtle
import time
import random
import threading
#from bonus_clock import Clock



#tim = Turtle(shape="square")
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")


turtle.tracer(1,0)
tim_seg = []
position = [(0,0),(-20,0),(-40,0)]
color_list = ["purple","green", "orange"]
for i in range(0,3,1):
    tim = Turtle(shape="square")
    tim.color(color_list[i])
    tim.penup()
    tim.goto(position[i])
    tim_seg.append(tim)
    





def right_():
    tim_seg[0].penup()
    if tim_seg[0].heading() != 180:
        tim_seg[0].setheading(0)
            
def up():
    tim_seg[0].penup()
    if tim_seg[0].heading() != 270:
        tim_seg[0].setheading(90)

def down():
    tim_seg[0].penup()
    if tim_seg[0].heading() != 90:
        tim_seg[0].setheading(270)

def left_():
    tim_seg[0].penup()
    if tim_seg[0].heading() != 0:
        tim_seg[0].setheading(180)
    
screen.listen()

screen.onkey(right_, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left_, "Left")



def over(head):
    if head.xcor() > 265: 
        return False
    elif head.xcor() < -281:
        return False
    elif head.ycor() > 280:
        return False
    elif head.ycor() < -265:
        return False
    else:
        return True

def game_end_star(position):
# set screen
    t = turtle.Turtle()
    t.shape()
    
    # decide colors

    
    # decide pensize
    t.pensize(1)
    turtle.tracer(0)
    # Draw star pattern
    # turtle.penup()
    t.setpos(position)
    t.pendown()
    for i in range(7):
        t.pencolor("red")
        t.forward(50)
        t.right(144)
    t.penup()
    t.hideturtle()
    turtle.tracer(1)  


food = turtle.Turtle(shape = "circle")
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.color("red")
food.penup()
food.speed("fastest")
x_food = random.randint(-260,260)
y_food = random.randint(-260,260)
food.goto(x_food, y_food)

with open("21/ping_pong_game/snake_project/highest_score.txt", "r") as f:
    highest = int(f.read())
f.close()
def game_over_display(score):
    turtle.color("white")
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(-70,0)
    #turtle.tracer(0,0)
    turtle.write('GAME OVER', move= False, font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(-40,-20)
    turtle.write(f'Score: {score}', move= False, font=("Arial", 20, "normal"))
    turtle.hideturtle()

#bonus_decay = Clock()
count_ = 1
score = 0
playing = True
while playing:
    screen.update()
    time.sleep(0.09)
    for index in range(len(tim_seg)-1, 0, -1):
        tim_seg[index].goto(tim_seg[index-1].pos())
    tim_seg[0].forward(20)
    turtle.color("white")
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(-50,280)
    #turtle.tracer(0,0)
    turtle.write(f'Score: {score}', move= False, font=("Arial", 14, "normal"))
    turtle.hideturtle()
    if tim_seg[0].distance(food) < 15:
        print("yaaas")
        turtle.clear()
        score = score+1
        new_turtle = turtle.Turtle()
        #new_turtle.hideturtle()
        new_turtle.shape("square")
        new_turtle.color(random.choice(color_list))
        new_turtle.penup()
        new_turtle.speed("fastest")
        #new_turtle.goto()
        #new_turtle.showturtle()
        tim_seg.append(new_turtle)
        x_food = random.randint(-260,260)
        y_food = random.randint(-260,260)
        if count_ % 5 == 0:
            food.shape("circle")
            food.shapesize(stretch_len=1.2,stretch_wid=1.2)
            score = score+1
            #t5.hideturtle()

        else:
            food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        food.goto(x_food, y_food)
        count_ = count_+1
        print(count_)
    #print(tim_seg[0].pos())
    #print(over(tim_seg[0]))
    playing = over(tim_seg[0])
    if playing == False:
        star_x, star_y =  tim_seg[1].pos()
        game_end_star((star_x-30, star_y+10))
        turtle.color("white")
        turtle.speed("fastest")
        turtle.penup()
        turtle.goto(-70,0)
        #turtle.tracer(0,0)
        turtle.write('GAME OVER', move= False, font=("Arial", 20, "normal"))
        turtle.penup()
        turtle.goto(-40,-20)
        turtle.write(f'Score: {score}', move= False, font=("Arial", 20, "normal"))
        turtle.hideturtle()
    
    for i in range(1, len(tim_seg),1):
        if tim_seg[0].distance(tim_seg[i]) < 15:
            print("collide") 
            playing = False
            game_over_display(score)
        
    if score > highest:
        if playing == False:
            with open("21/ping_pong_game/snake_project/highest_score.txt", "w") as f:
                f.write(str(score))
                f.close()           
                turtle.color("white")
                turtle.speed("fastest")
                turtle.penup()
                turtle.goto(-70,-40)
                turtle.write(f'Highest Score!!!', move= False, font=("Arial", 20, "normal"))
                turtle.hideturtle()
    
screen.exitonclick()