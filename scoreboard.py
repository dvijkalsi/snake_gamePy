from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_gamePy\data.txt") as data:
            d = data.read()
            if d == "":
                self.high_score = 0
            else:
                self.high_score = int(d)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_gamePy\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0    
        self.update_score()
        