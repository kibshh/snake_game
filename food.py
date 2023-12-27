from turtle import Turtle
import random
import config


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(config.FOOD_SIZE, config.FOOD_SIZE)
        self.color(config.FOOD_COLOR)
        self.speed("fastest")
        self.generate_new_food()

    def generate_new_food(self):
        randomx = random.randint((-int(config.SCREEN_WIDTH / 2) + 30), int(config.SCREEN_WIDTH / 2) - 30)
        randomy = random.randint((-int(config.SCREEN_HEIGHT / 2) + 30), int(config.SCREEN_HEIGHT / 2) - 30)
        self.goto(randomx, randomy)
