from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0 ,250)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, "center", FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", True, "center", FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0 ,250)
        self.update_scoreboard()