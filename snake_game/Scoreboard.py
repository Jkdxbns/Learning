from turtle import Turtle
POSITION = 0, 280 
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(POSITION)
        self.color("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = "center", font = FONT)
         

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        new_font =list(FONT)
        new_font[1] = 24
        self.home()
        self.write("Game Over.", align = "center", font = new_font)
        
