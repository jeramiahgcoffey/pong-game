from turtle import Turtle
FONT = ("Courier", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.left_score = 0
        self.right_score = 0
        self.write(f"Score: {self.left_score}     Score: {self.right_score}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.left_score}     Score: {self.right_score}", align="center", font=FONT)