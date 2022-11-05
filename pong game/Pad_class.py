from turtle import Turtle

class Pad(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square") 
        self.color("white")
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()

        
    def up(self):
        # self.setheading(90)
        self.forward(20)
        
    def down(self):
        # self.setheading(270)
        self.backward(20)
        
