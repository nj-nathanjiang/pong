import turtle as t


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto((x, y))

    def bounce_wall(self):
        self.y_move = -self.y_move

    def bounce_paddle(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset_ball(self):
        self.color("black")
        self.move_speed = 0.1
        self.goto(0, 0)
        self.color("white")
