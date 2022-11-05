from turtle import Turtle, Screen

# juego para dibujar usando el modulo Turtle


tim = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def turn_right():
    tim.right(10)
    
def turn_left():
    tim.left(10)
    
def reset_all():
    tim.reset()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=reset_all, key="c")

# cuando meto una funcion aca no se usan parentesis, los aprentesis son 
# para activar una funcion justo donde esta
screen.exitonclick()

# higher order function son funciones que usan otras funciones como arametros
