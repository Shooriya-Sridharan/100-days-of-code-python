import ball
import center
import paddle
import score
import turtle

WIDTH = 800
HEIGHT = 600

PADDLE_RIGHT_X = 370
PADDLE_LEFT_X = -370

P1_X = -200
P1_Y = 250

P2_X = 200
P2_Y = 250

X_SPEED = 0.5
Y_SPEED = 0.5

screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")

middle = center.Center()
middle.draw_line()

pong_ball = ball.Ball()

right_paddle = paddle.Paddle(PADDLE_RIGHT_X)
left_paddle = paddle.Paddle(PADDLE_LEFT_X)
score_p1 = score.Score(P1_X, P1_Y)
score_p1.initial_display("P1", 0)
score_p2 = score.Score(P2_X, P2_Y)
score_p2.initial_display("P2", 0)

curr_score_1 = 0
curr_score_2 = 0
game_is_on = True


def end_game(player):
    game_over = score.Score()
    pong_ball.hideturtle()
    screen.update()
    game_over.game_over(player)
    return False


while game_is_on:
    screen.update()
    if curr_score_1 == 5:
        game_is_on = end_game("P1")
    elif curr_score_2 == 5:
        game_is_on = end_game("P2")

    if pong_ball.is_right_wall_hit():
        curr_score_1 += 1
        score_p1.increase_score("P1", curr_score_1)
        pong_ball.hideturtle()
        del pong_ball
        pong_ball = ball.Ball()
    if pong_ball.is_left_wall_hit():
        curr_score_2 += 1
        score_p2.increase_score("P2", curr_score_2)

        pong_ball.hideturtle()
        del pong_ball
        pong_ball = ball.Ball()

    if pong_ball.is_top_wall_hit():
        Y_SPEED = -Y_SPEED
    elif right_paddle.is_paddle_hit(pong_ball, "right"):
        X_SPEED = -X_SPEED
    elif pong_ball.is_bottom_wall_hit():
        Y_SPEED = abs(Y_SPEED)
    elif left_paddle.is_paddle_hit(pong_ball, "left"):
        X_SPEED = abs(X_SPEED)
        Y_SPEED = abs(Y_SPEED)
    pong_ball.move(X_SPEED, Y_SPEED)

    screen.listen()
    screen.update()
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")
    screen.update()

screen.exitonclick()
