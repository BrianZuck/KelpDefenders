from turtle import RawTurtle
STARTING_POS = (-250,0)



class Player(RawTurtle):
    def __init__(self,screen):
        super().__init__(screen)
        self.shape("turtle")
        self.penup()
        self.gotostart()
        self.color("green")


    def gotostart(self):
        self.goto(STARTING_POS)


    def go_up(self):
        self.setheading(90)
        self.forward(20)
        self.setheading(0)

    def go_down(self):
        self.setheading(270)
        self.forward(20)
        self.setheading(0)

    def bounds(self):
        if self.ycor() > 300:
            self.goto(y=300, x=-250)
        if self.ycor() < -300:
            self.goto(y=-300, x=-250)

