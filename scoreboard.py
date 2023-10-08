from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score} ", align= "center", font=("Arial",15, "normal"))
        self.hideturtle()

    def count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align= "center", font=("Arial",15, "normal"))
    
    def end(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f"Game Over!", align= "center", font=("Arial",30, "normal"))

        



