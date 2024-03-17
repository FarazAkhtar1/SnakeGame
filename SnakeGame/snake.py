import time
from turtle import Turtle
MOVE_DISTANCE = 20

class Snake():
    def __init__(self) -> None:
        self.segments =[]
        i = 0
        for _ in range(3):
            every_turtle = Turtle("square")
            every_turtle.penup()
            every_turtle.color("white")
            every_turtle.goto(x= 0-i,y=0)
            i += 20
            self.segments.append(every_turtle)
            self.head = self.segments[0]

        print(self.segments)

    def add_segment(self, position):
        every_turtle = Turtle("square")
        every_turtle.penup()
        every_turtle.color("white")
        every_turtle.goto(position)
        self.segments.append(every_turtle)
        self.head = self.segments[0]
        
    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        i = 0
        for _ in range(3):
            every_turtle = Turtle("square")
            every_turtle.penup()
            every_turtle.color("white")
            every_turtle.goto(x= 0-i,y=0)
            i += 20
            self.segments.append(every_turtle)
            self.head = self.segments[0]

    
    def move(self):
       
        for seg_num in range(len(self.segments) - 1, 0, -1):
            pos_of_second_last = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(pos_of_second_last) 
        self.head.forward(MOVE_DISTANCE)
           
    def move_up(self):
        if self.head.heading() == 0.0 or self.head.heading() == 180.0:
            self.head.setheading(90.0)

    def move_right(self):
        if self.head.heading() == 90.0 or self.head.heading() == 270.0:
            self.head.setheading(0.0)

    def move_down(self):
        if self.head.heading() == 0.0 or self.head.heading() == 180.0:
            self.head.setheading(270.0)

    def move_left(self):
        if self.head.heading() == 90.0 or self.head.heading() == 270.0:
            self.head.setheading(180.0)

    

