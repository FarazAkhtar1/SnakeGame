from turtle import Turtle
 
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        self.score = 0
        with open("Projects\SnakeGame\data.txt") as highscorefile:
            self.high_score = int(highscorefile.read())
        self.write(f"Scoreboard: {self.score}, High score: {self.high_score}", align= "center", font= ("Courier", 16))

    def score_update(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Scoreboard: {self.score}, High Score: {self.high_score}", align= "center", font= ("Courier", 16))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Projects\SnakeGame\data.txt", mode= "w") as highscorefile:
                highscorefile.write(str(self.score))
        
        self.score = 0 
        self.clear()
        self.write(f"Scoreboard: {self.score}, High Score: {self.high_score}", align= "center", font= ("Courier", 16))
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align= "center", font= ("Courier", 20))
