import turtle as t
import paddle as p
import ball as b
import time
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
right_paddle = p.Paddle((350, 0))
left_paddle = p.Paddle((-350, 0))
ball = b.Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.distance(right_paddle.the_turtle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

    if ball.distance(left_paddle.the_turtle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_score += 1
        scoreboard.clear()
        scoreboard.write_scores()
        ball.bounce_paddle()

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_score += 1
        scoreboard.clear()
        scoreboard.write_scores()
        ball.bounce_paddle()

    if scoreboard.r_score == 10 or scoreboard.l_score == 10:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

screen.exitonclick()
