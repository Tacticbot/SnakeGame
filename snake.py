from turtle import Turtle
from food import Food
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
class Snake:
    def __init__(self) -> None:
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    
    def create_snake(self):
        for position in STARTING_POSITION:
            new = Turtle("square")
            new.penup()
            new.color("red")
            new.goto(position)
            self.segments.append(new)
    
    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()== 0:
            self.head.left(90)

        if self.head.heading()==180:
            self.head.right(90)
    
    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
            
        if self.head.heading() == 180:
            self.head.left(90)
    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
            
        if self.head.heading() == 270:
            self.head.right(90)
        

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
            
        if self.head.heading() == 270:
            self.head.left(90)


    def grow(self):
        new = Turtle("square")
        new.penup()
        new.color("red")
        new_x = self.segments[len(self.segments)-1].xcor()
        new_y = self.segments[len(self.segments)-1].ycor()
        new.goto(new_x, new_y)
        self.segments.append(new)
