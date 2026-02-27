import random
import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
import time
from scoreboard import Scoreboard

window = turtle.Screen()
window.title('Break-out game')
window.setup(800,600)
window.bgcolor('black')
window.tracer(0)

color = ["red", "orange", "yellow", "green", "blue"]
bricks = []

paddle = Paddle((0,-250))
ball = Ball()
scoreboard = Scoreboard()

message = turtle.Turtle()
message.hideturtle()
message.color("white")
message.penup()

def build_bricks():
    global bricks
    for row in range(5):
        for col in range(8):

            x = -300 + col * 80
            y = 200 - row * 40

            brick = Brick((x, y), random.choice(color))
            bricks.append(brick)


window.listen()
window.onkey(paddle.go_left, "Left")
window.onkey(paddle.go_right, "Right")
window.onkey(paddle.go_left, "w")
window.onkey(paddle.go_right, "s")

build_bricks()
game_is_on = True
highest_speed = 0.003

#display message
def show_message(text):
    message.clear()
    message.goto(0, 0)
    message.write(text, align="center", font=("Arial", 36, "bold"))

while game_is_on:
    time.sleep(ball.move_speed)
    window.update()
    ball.move()
    scoreboard.update_scoreboard()

    #detect collision with wall
    if ball.ycor() < -290:
        game_is_on = False
    if ball.ycor() > 290:
        ball.bounce_y()
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

        #paddle detection with ball
    if ball.distance(paddle) < 50 and ball.y_move < 0:
        ball.bounce_y()
        offset = ball.xcor() - paddle.xcor()
        ball.x_move = offset / 8


    #ball detection with bricks
    for brick in bricks:
        if ball.distance(brick) < 40:
            ball.bounce_y()
            brick.goto(1000, 1000)
            bricks.remove(brick)
            if ball.move_speed > highest_speed:
                ball.move_speed *= 0.72

#display win after all bricks remove
    if not bricks:
        show_message("YOU WIN!")
        time.sleep(2)
        message.clear()
        ball.reset_position()
        scoreboard.reset_timer()
        bricks.clear()
        build_bricks()

window.exitonclick()