from turtle import Turtle
import turtle

SPEED = 10
INITIAL_COLOR = "red"
COLOR = "white"
SHAPE = "square"
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
WIDTH = 600
HEIGHT = 600


class Snake:
    START = 1
    turtles = []

    def __init__(self):

        new_turtle = Turtle(SHAPE)
        new_turtle.color(INITIAL_COLOR)
        new_turtle.penup()
        self.turtles.append(new_turtle)
        for i in range(2):
            new_turtle = Turtle("square")
            new_turtle.color(COLOR)
            new_turtle.penup()
            new_turtle.goto(self.turtles[i].xcor() - 20, new_turtle.ycor())
            self.turtles.append(new_turtle)

    def increase(self):
        self.START += 1

        new_turtle = Turtle("square")
        new_turtle.color(COLOR)
        new_turtle.penup()
        new_turtle.goto(self.turtles[len(self.turtles) - 1].xcor() - 20, new_turtle.ycor())
        self.turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)

        self.turtles[0].forward(SPEED)

    def turn_right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def turn_left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def is_game_over(self):
        return (self.turtles[0].xcor() >= WIDTH / 2 - 20 or self.turtles[0].xcor() <= -WIDTH / 2 + 20) or (
                self.turtles[0].ycor() >= HEIGHT / 2 - 20 or self.turtles[
            0].ycor() <= -HEIGHT / 2 + 20) or self.is_body_hit()

    def is_body_hit(self):
        for i in self.turtles[1:]:
            if self.turtles[0].distance(i) < 8:
                return True
