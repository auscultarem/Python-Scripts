from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the animation and we control the screen with a while loop.

snake = Snake()  # creates an object snake
food = Food()  # creates an object food
scoreboard = ScoreBoard()  # creates an object scoreboard

screen.listen()  # This part detect an event on the screen
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  # Update the screen and refresh the anomation.
    time.sleep(0.1)

    snake.move()  # snake Move
    # Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()

    # Detect Colision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = scoreboard.game_over()

    # Detect Colison with tail
    # if head collids with any segment in the tail
    # trigger game over
    for segment in snake.segments:  # this sentene can be changed by: for segment in snake.segment[1:]: nad remove
        # lines 46 nad 47
        if segment == snake.head:  # segment[0] will be equal to snake.head so we have to ignore the snake.head and
            # continue
            pass
        elif snake.head.distance(segment) < 10:  # if snake.head distance is near to the body the game is over
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
