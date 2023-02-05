from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

l_score = ScoreBoard((-50, 250))
r_score = ScoreBoard((50, 250))




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)
    
    ball.move()

    # Detect collision with wall 
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()
    
    # Detect collision with padel
    if ((ball.distance(r_paddle) < 50) and (ball.xcor() > 320)) or ((ball.distance(l_paddle) < 50) and (ball.xcor() < -320)):
        ball.bounce_x()
    
    # Detect out of bounds
    if (ball.xcor() > 380):
        l_score.update_score()
        ball.reset()
    
    if (ball.xcor() < -380):
        r_score.update_score()
        ball.reset()







    




screen.exitonclick()