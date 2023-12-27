from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 350)
        self.write(f"SCORE: {self.current_score}", align="center", font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.current_score += 1
        self.refresh_score()

    def game_over(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 20, 'normal'))
