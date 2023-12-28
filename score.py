from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt", mode="r") as score_file:
            self.high_score = int(score_file.read())
        self.game_over_flag = False
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 350)
        self.write(f"SCORE: {self.current_score} HIGH SCORE: {self.high_score}",
                   align="center", font=('Courier', 20, 'normal'))
        self.goto(300, -370)
        self.write("press 'q' to quit", align="center", font=('Courier', 10, 'normal'))
        self.goto(0, 350)

    def increase_score(self):
        self.current_score += 1
        self.refresh_score()

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
        self.current_score = 0
        self.refresh_score()

    def game_over(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 0)
        self.write("THANK YOU FOR PLAYING OUR GAME", align="center", font=('Courier', 20, 'normal'))
        self.goto(0, -50)
        self.write("press anywhere on the screen to exit", align="center", font=('Courier', 10, 'normal'))
        self.game_over_flag = True
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
