from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("blue")
        self.speed("fastest")
        x_cor = random.randint(-280,280)
        y_cor = random.randint(-280,280)
        self.goto(x_cor, y_cor)
    
    def random_location_of_food(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))