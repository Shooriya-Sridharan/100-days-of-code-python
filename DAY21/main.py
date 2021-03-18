import time, food, scorecard, gameover
from turtle import Screen

from snake import Snake

WIDTH = 600
HEIGHT = 600
turtles = []
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("snek")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

game_is_on = True
food_pos = food.Food().food()
score = 0
score_card = scorecard.Score()
while game_is_on:
    screen.listen()
    if snake.is_game_over():
        gameover.GameOver()
        game_is_on = False
    screen.update()
    time.sleep(0.08)
    snake.move()
    screen.onkeypress(snake.up, "w")
    screen.onkeypress(snake.down, "s")
    screen.onkeypress(snake.turn_right, "d")
    screen.onkeypress(snake.turn_left, "a")

    snake_x = int(snake.turtles[0].xcor())
    snake_y = int(snake.turtles[0].ycor())

    if ((snake_x + 20) >= food_pos[0] >= (snake_x - 20)) and (snake_y + 20 >= food_pos[1] >= snake_y - 20):
        snake.increase()
        score += 1
        score_card.increase_score(score)

        food_pos = food.Food().food()
        screen.update()

screen.exitonclick()
