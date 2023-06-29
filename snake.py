from turtle import Turtle
STARTING_POSTIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        # to make the "head" easier to access
        self.head = self.segments[0]
        self.length = len(self.segments)
    
    def create_snake(self):
        for position in STARTING_POSTIONS:
            if position == (0,0):
                new_segment = Turtle(shape="triangle")
            else:
                new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)   
            
    def extend(self):
        self.add_segment(self.segments[-1].position())
            
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(), self.segments[seg_num-1].ycor())
        self.segments[0].forward(20)

        
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)
        
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)
        
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)
        
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.length = len(self.segments)
    
            
        
    
    