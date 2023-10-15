from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score}  HighScore: {self.highscore}", align= "center", font=("Arial",15, "normal"))
        

    def count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align= "center", font=("Arial",15, "normal"))

        
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        
    
    def end(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f"Game Over!", align= "center", font=("Arial",30, "normal"))
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")

        



