from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
# Estos ultimos 3 metodos vienen de la clase turtle y solo los podemos usar
# porque inicializamos turtle como superclase.
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
