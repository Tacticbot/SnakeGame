from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

move = True
while move:
    screen.update()
    time.sleep(0.1)


    snake.move()
    for i in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[i]) < 10:
            score.end()
            move =False
    if (snake.head.xcor() >= 290 or snake.head.xcor() <= -290) or (snake.head.ycor() >= 290 or snake.head.ycor() <= -290):
        score.end()
        move = False
    if snake.head.distance(food) <15:
        food.refresh()
        if food.refresh:
            score.count()
            snake.grow()

    


screen.exitonclick()