import turtle as t


class Paddle:

    def __init__(self, coordinates):
        self.the_turtle = t.Turtle(shape="square")
        self.the_turtle.penup()
        self.the_turtle.shapesize(stretch_wid=5, stretch_len=1)
        self.the_turtle.goto(coordinates)
        self.the_turtle.color("white")

    def go_up(self):
        new_y = self.the_turtle.ycor() + 20
        self.the_turtle.goto(self.the_turtle.xcor(), new_y)

    def go_down(self):
        new_y = self.the_turtle.ycor() - 20
        self.the_turtle.goto(self.the_turtle.xcor(), new_y)
