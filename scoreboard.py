from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.start_time = time.time()
        self.elapsed_time = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.elapsed_time = int(time.time() - self.start_time)
        self.goto(0, 220)
        self.write(f"Time: {self.elapsed_time}s",align="center",font=("Courier", 24, "normal"))

    def reset_timer(self):
        self.start_time = time.time()
        self.update_scoreboard()
