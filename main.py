from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle((-350, 0))
paddle_two = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_two.go_up, "Up")
screen.onkey(paddle_two.go_down, "Down")
screen.onkey(paddle_one.go_up, "w")
screen.onkey(paddle_one.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
        
    # Detect collision with paddle_one
    if ball.distance(paddle_one) < 55 and ball.xcor() < -320:
        ball.paddle_bounce()
        
    # Detect collision with paddle_two
    if ball.distance(paddle_two) < 55 and ball.xcor() > 320:
        ball.paddle_bounce()
        
    # Detect out of bounds on right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    # Detect out of bounds on left    
    if ball.xcor() < -380:
        ball.reset_position()   
        scoreboard.r_point()  

screen.exitonclick()