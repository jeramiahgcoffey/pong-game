from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_factor = 10
        self.y_factor = 10
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_factor
        new_y = self.ycor() + self.y_factor
        self.goto(new_x, new_y)
        time.sleep(self.speed)

    def wall_bounce(self):
        self.y_factor *= -1

    def paddle_bounce(self):
        self.x_factor *= -1

    def reset_ball(self):
        self.goto((0, 0))
        time.sleep(1)
        self.x_factor *= -1

    def increase_speed(self):
        if self.speed > 0.004:
            self.speed -= 0.005

    def reset_speed(self):
        if self.speed <= 0.05:
            self.speed = 0.05
        else:
            self.speed = 0.075
