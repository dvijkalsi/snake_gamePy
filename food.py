import random
from turtle import Turtle
import turtle as t

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        t.colormode(255)
        self.penup()
        self.shape("turtle")
        #self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        
    def refresh(self):
        self.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.left(random.choice([0,90,180,270]))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
    