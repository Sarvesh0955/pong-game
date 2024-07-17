from turtle import Turtle


def dotted_line():
    doted_line = Turtle()
    doted_line.color("white")
    doted_line.hideturtle()
    doted_line.penup()
    doted_line.seth(90)
    doted_line.goto(0, -300)
    for i in range(0, 16, 1):
        doted_line.pendown()
        doted_line.forward(40)
        doted_line.penup()
        doted_line.forward(40)


class Scoreboard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(pos)
        self.print_score()

    def print_score(self):
        self.write(f"{self.score}", align="center")

    def update(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self, player):
        self.goto(0,0)
        self.write(f"player {player} won")
