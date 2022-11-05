from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
streets = [-240, -210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210, 240]
all_cars = []

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square") 
        self.color("white")
        self.shapesize(1, 5)

            
            