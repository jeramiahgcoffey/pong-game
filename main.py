from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Initialize screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.listen()
screen.tracer(0)

# Create paddle objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Create ball object
ball = Ball()

# Create scoreboard
score = Scoreboard()

# Game controls
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


# Starts game
game_on = True
while game_on:
    screen.update()
    ball.move()
    # Bounce off wall
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.wall_bounce()
    # Bounce off paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()
        ball.increase_speed()
    # Out of bounds
    if ball.xcor() > 350:
        score.left_point()
        ball.goto(0,0)
        screen.update()
        ball.reset_speed()
        ball.reset_ball()
    if ball.xcor() < -350:
        score.right_point()
        ball.goto(0, 0)
        screen.update()
        ball.reset_speed()
        ball.reset_ball()


screen.exitonclick()
