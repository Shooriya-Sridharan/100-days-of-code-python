import turtle

WIDTH = 380
HEIGHT = 280


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, x_new, y_new):
        x = self.xcor() + x_new
        y = self.ycor() + y_new
        self.goto(x, y)

    def is_top_wall_hit(self):
        return self.ycor() >= HEIGHT

    def is_bottom_wall_hit(self):
        return self.ycor() <= -HEIGHT

    def is_right_wall_hit(self):
        self.clear()
        return self.xcor() >= WIDTH

    def is_left_wall_hit(self):
        return self.xcor() <= -WIDTH
