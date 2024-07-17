from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard, dotted_line
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard1 = Scoreboard((20, 280))
scoreboard2 = Scoreboard((-20, 280))
dotted_line()

paddle1 = Paddle()
paddle1.move_to(paddle1.POS_1)

paddle2 = Paddle()
paddle2.move_to(paddle2.POS_2)

ball = Ball()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ct = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if paddle1.distance(ball) < 40 and ball.xcor() < -375:
        ball.collide()
        ball.move()
        continue

    if paddle2.distance(ball) < 40  and ball.xcor() > 375:
        ball.collide()
        ball.move()
        continue

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        ball.move()
        continue

    if ball.xcor() < -380:
        scoreboard1.update()
        ball.pos_reset()
        continue

    if ball.xcor() > 380:
        scoreboard2.update()
        ball.pos_reset()
        continue

    if scoreboard1.score == 5:
        game_is_on = False
        scoreboard1.game_over(1)

    if scoreboard1.score == 1:
        game_is_on = False
        scoreboard2.game_over(2)


screen.exitonclick()
