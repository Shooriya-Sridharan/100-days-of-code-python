import turtle

BOUND_Y = 235
PADDLE_WIDTH = 20


class Paddle(turtle.Turtle):
    def __init__(self, X):
        self.x = X
        super().__init__()
        self.goto(self.x, y=4)
        self.color("white")
        self.shape("square")
        self.penup()
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        if self.ycor() < BOUND_Y:
            y_cor = self.ycor() + 20
            self.goto(self.xcor(), y_cor)

    def move_down(self):
        if self.ycor() > -BOUND_Y:
            y_cor = self.ycor() - 20
            self.goto(self.xcor(), y_cor)

    def is_paddle_hit(self, lil_ball, paddle_side):
        if paddle_side == "right":
            return lil_ball.distance(self) < 50 and lil_ball.xcor() >= self.x - PADDLE_WIDTH
        return lil_ball.distance(self) < 30 and lil_ball.xcor() <= self.x + PADDLE_WIDTH
