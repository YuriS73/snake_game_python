import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed(10)
        self.refresh()

    def refresh(self):
        random_x = round(random.randint(-280, 280) / 10) * 10
        random_y = round(random.randint(-280, 280) / 10) * 10
        self.goto(random_x, random_y)
