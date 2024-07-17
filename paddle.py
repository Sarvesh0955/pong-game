from turtle import Turtle


class Paddle(Turtle):
    POS_1 = (-390, 0)
    POS_2 = (380, 0)

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.seth(90)
        self.shapesize(stretch_len=5, stretch_wid=1)

    def move_to(self, pos):
        self.goto(pos)

    def up(self):
        self.seth(90)
        self.forward(20)

    def down(self):
        self.seth(270)
        self.forward(20)
