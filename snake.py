from turtle import Turtle
import config

SEGMENT_SIZE = 1.5
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for i in range(3):
            self.add_segment(-i * 20 * SEGMENT_SIZE, 0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20 * SEGMENT_SIZE)

    def add_segment(self, coordinatex, coordinatey):
        segment = Turtle(config.SNAKE_SHAPE)
        segment.color(config.SNAKE_COLOR)
        segment.shapesize(SEGMENT_SIZE)
        segment.penup()
        segment.setpos(coordinatex, coordinatey)
        self.segments.append(segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def reset(self):
        for seg in self.segments:
            seg.goto(1200,1200)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    def game_over(self):
        for seg in self.segments:
            seg.goto(1200, 1200)
        self.segments.clear()
