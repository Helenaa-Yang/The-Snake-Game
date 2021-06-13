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
        with open("HighestScore.txt", mode="r") as file:
            new_highest_score = int(file.read())
        # self.highest_score = 0
        self.highest_score = new_highest_score
        self.update_scoreboard()
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))   可再精簡改def

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest: {self.highest_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))   可再精簡改def

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("HighestScore.txt", mode="w") as file:
            file.write(f"{self.highest_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

