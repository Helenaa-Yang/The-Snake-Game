from turtle import Turtle

ALIGNMENT = "center"              #之後想改數值方便哈哈XDD
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))   可再精簡改def

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))   可再精簡改def

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

