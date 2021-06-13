START_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # constant放上面，並在class中改caps
MOVE_POSITION = 20  # 放在這邊的目的就是希望到時候能方便調整這些常數
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle

class Snake():
    def __init__(self):
        self.segment = []  # variable 加上 call object 的 self.
        self.create_snake()  # 呈現最初始狀態
        self.head = self.segment[0]  # 很常呼叫第一個方塊所以新增一個variable給他

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)  # 從這邊發現self.segment為 Turtle 的 object list

    def extend_segment(self):
        self.add_segment(self.segment[-1].position())  ##########我沒有理解這個我以為這個位子是最後一個segment，那怎麼會多呢????

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seg - 1].xcor()
            y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x, y)
        self.head.forward(MOVE_POSITION)

    def reset(self):
        for seg in self.segment:         #self.segment為 Turtle 的 object list
            seg.goto(1000, 1000)         #所以才可以用 Turtle 的 function
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]   #你可以玩玩看，刪掉他你就知道到底是怎麼運作了

    def up(self):
        if self.head.heading() != DOWN:  # 把它變成常數才能比大小唷
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

