from turtle import Turtle, Screen
import random
import time
from Scoreboard_Class import Scoreboard

screen = Screen()
screen.title("TurtleCrossing Game")
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.tracer(0) 


tim = Turtle(shape="turtle")
tim.color("green")
tim.penup()
tim.goto(0, -270)
tim.setheading(90)
scoreboard = Scoreboard()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
streets = [-240, -210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210, 240]
all_cars = []

def up():
    tim.forward(30)

def traffic():
    for car_index in range(0, random.randint(0, 2)):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(colors))
        new_car.goto(x=-300, y=random.choice(streets))
        all_cars.append(new_car)

screen.listen()
screen.onkey(up, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    traffic()
    for car in all_cars:
        car.forward(20)
        if car.distance(tim)<10:
            game_is_on=False
            scoreboard.game_over()
        if tim.ycor() == 270:
            scoreboard.increase_score()
            tim.goto(0, -270)
            tim.setheading(90)




       
    
    
    
screen.exitonclick()






























screen.exitonclick()