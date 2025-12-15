from turtle import Turtle, RawTurtle

FONT = ("Courier", 22, "normal")


class Scoreboard(RawTurtle):
    def __init__(self,screen):
        super().__init__(screen)
        self.screen = screen
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-265, 250)
        self.money = 0
        self.killcount = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} Bank: {self.money} Kills: {self.killcount}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
        #enemies.goto(x = -290, y= 0)

    def add_bank(self):
        self.money += 50
        self.update_scoreboard()

    def increase_kill(self):
        self.killcount += 1
        self.update_scoreboard()

    def winner(self):
        self.goto(0, 0)
        self.write(f"YOU WIN!", align="center", font=FONT)

    def score_reset(self):
        self.level = 1
        self.money = 0
        self.killcount = 0
        self.goto(-265, 250)
        self.update_scoreboard()
