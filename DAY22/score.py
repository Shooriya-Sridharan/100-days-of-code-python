import turtle


class Score(turtle.Turtle):
    def __init__(self, X=0, Y=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(X, Y)

    def initial_display(self, player, score):
        self.write(f"{player}:{score}", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self, player, curr_score):
        self.clear()
        self.write(f"{player}:{curr_score}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self, winner):
        self.write(f"Game over {winner} wins", move=False, align="center", font=("Arial", 24, "normal"))
