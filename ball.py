from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.random_dir()

    def move(self):
        self.forward(20)

    def random_dir(self):
        rand_angle_1 = randint(-75, 75)
        rand_angle_2 = randint(105, 255)
        choice = randint(0,1)
        if choice == 1:
            self.seth(rand_angle_1)
        else:
            self.seth(rand_angle_2)

    def collide(self):
        cur_angle = self.heading()
        if 0 <= cur_angle < 90:
            ref_angle = cur_angle
            self.left(180 - 2 * ref_angle)
        elif 90 <= cur_angle < 180:
            ref_angle = 180 - cur_angle
            self.right(180 - 2 * ref_angle)
        elif 180 <= cur_angle < 270:
            ref_angle = cur_angle - 180
            self.left(180 - 2 * ref_angle)
        else:
            ref_angle = 360 - cur_angle
            self.right(180 - 2 * ref_angle)

    def bounce(self):
        cur_angle = self.heading()
        if 0 <= cur_angle < 90:
            ref_angle = 90 - cur_angle
            self.right(180 - 2 * ref_angle)
        elif 90 < cur_angle < 180:
            ref_angle = cur_angle - 90
            self.left(180 - 2 * ref_angle)
        elif 180 < cur_angle < 270:
            ref_angle = 270 - cur_angle
            self.right(180 - 2 * ref_angle)
        else:
            ref_angle = cur_angle - 270
            self.left(180 - 2 * ref_angle)

    def pos_reset(self):
        self.setpos(0, 0)
        self.random_dir()
