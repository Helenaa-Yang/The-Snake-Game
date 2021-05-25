from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):       #這邊就看出 inherit class 好用之處拉~~ 叫Turtle()裡面的 refresh()後，不僅清除資料並做self.的要求
        x_random = random.randint(-280, 280)    #What are you doing...... 寫反了拉白ㄘ
        y_random = random.randint(-280, 280)
        self.goto(x_random, y_random)


