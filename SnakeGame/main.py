from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import sys
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey( snake.move_up,"Up" )
screen.onkey( snake.move_down, "Down")
screen.onkey( snake.move_right, "Right")
screen.onkey( snake.move_left, "Left")

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.score_update()
        food.random_location_of_food()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:

        scoreboard.reset()
        snake.snake_reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print(snake.segments)

            scoreboard.reset()
            snake.snake_reset()
        

        
    



screen.exitonclick()