from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 1
        
    def move(self):
        new_x = self.xcor() + (self.x_move * self.speed)
        new_y = self.ycor() + (self.y_move * self.speed)
        self.goto(new_x, new_y)
        
    def wall_bounce(self):
        self.y_move *= -1
        
    def paddle_bounce(self):
        self.x_move *= -1
        self.speed *= 1.05
        
    def reset_position(self):
        self.goto(0,0)
        self.speed = 1
        self.paddle_bounce()