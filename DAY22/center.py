import turtle

X = 0
Y = 290


class Center(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.left(90)
        self.y = -Y
        # self.hideturtle()
        self.goto(X, -Y)

    def draw_line(self):
        while self.y <= Y:
            self.y += 20
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
