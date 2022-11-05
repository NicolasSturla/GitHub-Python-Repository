from turtle import Screen
import time
from snake import Snake
from snake_game_food_class import Food
from snake_game_scoreboard_class import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
# Detect colision with food, using distance method.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # detect colision with wall.
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()
        
    # detect colision with body-
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            

screen.exitonclick()