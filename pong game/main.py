from turtle import Turtle, Screen
from Pad_class import Pad
from Ball_Class import Ball
import time

screen = Screen()
screen.title("PingPong Game")
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)
# el comando tracer elimina todas las animaciones si lo ponemos en 0, pero al 
# hacer esto, tenemos que actualizar de forma manual la pantalla cada vez.
# hacemos esto con un "while" y con el metodo screen.update y time.sleep 


r_pad = Pad()
r_pad.goto(350, 0)
screen.listen()
screen.onkey(r_pad.up, "o")
screen.onkey(r_pad.down, "k")

l_pad = Pad()
l_pad.goto(-350, 0)
screen.listen()
screen.onkey(l_pad.up, "e")
screen.onkey(l_pad.down, "d")

ball = Ball()

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (r_pad.distance(ball) < 60 and ball.xcor() < 340) or (l_pad.distance(ball) < 60 and ball.xcor() > -340):
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_position()
        
    if ball.ycor() >380:
        ball.reset_position()
        ball.bounce_y()
        
        












screen.exitonclick()
