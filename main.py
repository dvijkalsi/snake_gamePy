from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
screen.title("Cooler Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
        
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        scoreboard.reset()
        snake.reset()
        #print("hit the wall")
        
        
    # Detect collision with tail
    # if head collides with any segment in the tail: trigger game_over
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    


screen.exitonclick()