from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
import config

screen = Screen()
screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
screen.bgcolor(config.BACKGROUND_COLOR)
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(scoreboard.game_over, "q")


game_on = True
while game_on:
    if scoreboard.game_over_flag:
        snake.game_over()
        game_on = False
        screen.update()
        continue
    screen.update()
    time.sleep(config.GAME_SPEED)
    snake.move()

    if (snake.head.xcor() > config.SCREEN_WIDTH / 2 or snake.head.xcor() < -(config.SCREEN_WIDTH / 2)
            or snake.head.ycor() > (config.SCREEN_HEIGHT / 2) or snake.head.ycor() < -(config.SCREEN_HEIGHT / 2)):
        scoreboard.reset_score()
        snake.reset()
        continue

    if snake.head.distance(food) < 20:
        food.generate_new_food()
        scoreboard.increase_score()
        snake.extend_snake()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 15:
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()
