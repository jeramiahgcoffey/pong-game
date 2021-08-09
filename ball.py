from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_factor = 10
        self.y_factor = 10

    def move(self):
        new_x = self.xcor() + self.x_factor
        new_y = self.ycor() + self.y_factor
        self.goto(new_x, new_y)
        time.sleep(0.1)

    def wall_bounce(self):
        self.y_factor *= -1

    def paddle_bounce(self):
        self.x_factor *= -1

    def reset_ball(self):
        self.goto((0, 0))
        time.sleep(1)
        self.x_factor *= -1