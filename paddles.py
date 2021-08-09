from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(position)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)

    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)