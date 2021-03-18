import turtle


class Score:

    def __init__(self):
        self.score = turtle.Turtle()
        self.score.hideturtle()
        self.score.color("white")
        self.score.penup()
        self.score.goto(0, 260)
        self.update_score(0)

    def update_score(self, curr_score):
        self.score.write(f"Score:{curr_score}", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self, new_score):
        self.score.clear()
        self.update_score(new_score)
