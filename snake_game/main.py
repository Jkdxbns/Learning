from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Scoreboard import ScoreBoard
import time


#Defining Screen
screen = Screen()
screen.screensize(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

#Draw Boundries
boundry = Turtle()
boundry.penup()
boundry.pencolor("white")
boundry.turtlesize(0.3)
boundry.goto((295, -295))
boundry.pendown()
boundry.goto((295, 280))
boundry.goto((-295, 280))
boundry.goto((-295, -295))
boundry.goto((295, -295))


#Creating Food and Snake Objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


#Check for user interaction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.refresh()

    #Detect Collision with wall
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>275 or snake.head.ycor()<-295:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with Tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.game_over()
            game_is_on = False

    
screen.exitonclick()





