#Making the Screen for the ping pong game
import turtle
import random

from sklearn.preprocessing import PolynomialFeatures
#from players import Player


screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.bgcolor("black")
screen.title("Ping Pong")
turtle.tracer(0)
demarcation_turtle = turtle.Turtle()
demarcation_turtle.color("white")
demarcation_turtle.penup()
demarcation_turtle.goto(0,200)
demarcation_turtle.pendown()
demarcation_turtle.right(90)
demarcation_turtle.speed("fastest")


#turtle.tracer(0)
while demarcation_turtle.ycor() > -190:
    demarcation_turtle.forward(10)
    demarcation_turtle.penup()
    demarcation_turtle.forward(10)
    demarcation_turtle.pendown()


color = "red"
player_1 = turtle.Turtle()
player_1.penup()
player_1.color(color)
player_1.speed("fastest")
player_1.shape("square")
player_1.shapesize(stretch_wid=0.3,stretch_len=2)
player_1.goto(-390,0)
player_1.left(90)
#player_1.speed("normal")

color = "red"
player_2 = turtle.Turtle()
player_2.penup()
player_2.color(color)
player_2.shape("square")
player_2.shapesize(stretch_wid=0.3,stretch_len=2.0)
player_2.goto(380,0)
player_2.left(90)
player_2.speed("fastest")
#player_2.speed("normal")



def up():
    player_1.setheading(90)
    if player_1.ycor() < 180:
        player_1.forward(30)
   
def down():
    player_1.setheading(270)
    if player_1.ycor() > -160.01:
        player_1.forward(30)
 

screen = turtle.Screen()
screen.listen()
screen.onkey(up, "w")
screen.onkey(down, "s")

def up():
    player_2.setheading(90)
    if player_2.ycor() < 180:
        player_2.forward(20)
   
def down():
    player_2.setheading(270)
    if player_2.ycor() > -160.01:
        player_2.forward(20)
    

screen = turtle.Screen()
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")


#Making the ball and making it bounce

ball = turtle.Turtle(shape="circle")
ball.color("white")
ball.penup()
ball.shapesize(0.5,0.5)
ball.speed('slowest')

player_1_score = 0
player_2_score = 0

def write_score(player_1_score, player_2_score):
    wr = turtle.Turtle()
    wr.color("white")
    wr.penup()
    wr.speed("fastest")
    wr.goto(-17,170)
    wr.write(f'{player_1_score}   {player_2_score}', move= False, font=("Arial", 20, "normal"))
    wr.hideturtle()


write_score(player_1_score, player_2_score)
turtle.tracer(1)


def check_for_collision():
    pass

p = random.choice([-185,185])
x = random.randint(-385,385)
y = random.randint(-185,185)
ball.goto(x,p)
if x < 0:
    ball.goto(-390,y)
else:
    ball.goto(380, y)

#screen.update()
on = True
while on:
    #screen.update()
    
    s = random.randint(-380,380)
    t = random.randint(-185,185)


    #turtle.hideturtle()
    
    if ball.xcor() > 0:
        ball.goto(random.randint(10,290),random.choice([-185,185]))
        one_or_mutiple_bounces = [1,2,3]
        bounce = random.choice(one_or_mutiple_bounces)
        if bounce == 1:
            if ball.ycor() == 185:
                ball.goto(random.randint(-270,-10),-185)
                ball.goto(-395,185)
            else:
                ball.goto(random.randint(-270,-10),185)
                ball.goto(-395,-185)
        elif bounce == 2:
            if ball.ycor() == 185:
                ball.goto(random.randint(-270,-10),-185)
                ball.goto(ball.xcor()-50,185)
                ball.goto(-390,-185)
            else:
                ball.goto(random.randint(-270,-10),185)
                ball.goto(ball.xcor()-40,-185)
                ball.goto(-390,185)
        else:
            if ball.ycor() == 185:
                ball.goto(random.randint(-270,-10),-185)
                ball.goto(ball.xcor()-50,185)
                ball.goto(ball.xcor()-20,-185)
                ball.goto(-390,185)
            else:
                ball.goto(random.randint(-270,-10),185)
                ball.goto(ball.xcor()-50,-185)
                ball.goto(ball.xcor()-20,185)
                ball.goto(-390,-185)
    
    else:
        ball.goto(random.randint(-350,-10),random.choice([-185,185]))
        one_or_mutiple_bounces = [1,2,3]
        bounce = random.choice(one_or_mutiple_bounces)
        if bounce == 1:
            if ball.ycor() == 185:
                ball.goto(random.randint(10,270),-185)
                ball.goto(390,185)
            else:
                ball.goto(random.randint(10,270),185)
                ball.goto(395,-185)
        elif bounce == 2:
            if ball.ycor() == 185:
                ball.goto(random.randint(10,270),-185)
                ball.goto(ball.xcor()+50,185)
                ball.goto(390,-185)
            else:
                ball.goto(random.randint(10,270),185)
                ball.goto(ball.xcor()+40,-185)
                ball.goto(390,185)
        else:
            if ball.ycor() == 185:
                ball.goto(random.randint(10,270),-185)
                ball.goto(ball.xcor()+50,185)
                ball.goto(ball.xcor()+20,-185)
                ball.goto(390,185)
            else:
                ball.goto(random.randint(10,270),185)
                ball.goto(ball.xcor()+50,-185)
                ball.goto(ball.xcor()+20,185)
                ball.goto(390,-185)
    
    
    
#write function for collission detection 
 





#print(playero)
screen.exitonclick()
