from snake_game_food_class import Food
FONT = ("Arial", 24, "normal")


class Scoreboard(Food):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0 ,250)
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, "center", FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.goto(0 ,250)
        self.score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", True, "center", FONT)

    def increase_score(self):
        self.score += 1
        self.goto(0 ,250)
        self.update_scoreboard()
        

            
            
            
            
            
            
            
            
            
            