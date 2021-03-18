import turtle


class GameOver:
    def __init__(self):
        self.game_over = turtle.Turtle()
        self.game_over.hideturtle()
        self.game_over.color("white")
        self.game_over.penup()
        self.game_over.write("Game Over", move=False, align="center", font=("Arial", 24, "normal"))
