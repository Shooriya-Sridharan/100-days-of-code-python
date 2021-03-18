import random,snake
import turtle

WIDTH = 600
HEIGHT = 600


class Food():
    lil_food = turtle.Turtle("circle")

    def __init__(self):
        # super().__init__()
        self.lil_food.speed("fastest")

    def food(self):
        self.lil_food.hideturtle()
        x = random.randint(-int(WIDTH / 2) + 30, int(WIDTH / 2) - 30)
        y = random.randint(-int(HEIGHT / 2) + 30, int(HEIGHT / 2) - 30)
        self.lil_food.color("white")
        self.lil_food.penup()
        self.lil_food.goto(x, y)
        self.lil_food.showturtle()
        return [x, y]
