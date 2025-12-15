from turtle import RawTurtle
ANGLES  = [40, 80, 120, 160, 200, 240, 280, 320, 360]

class Bomb:
    def __init__(self, screen):
        self.screen = screen
        self.shrapnels = []
        self.detonate = True

    def bomb_move(self, mousex, mousey, button):
        global ANGLES
        for i in range(0,9):
            button.grid_remove()
            shrapnel = RawTurtle(self.screen)
            shrapnel.hideturtle()
            shrapnel.color("orange")
            shrapnel.penup()
            shrapnel.goto(mousex, mousey)
            shrapnel.setheading(ANGLES[i])
            shrapnel.showturtle()
            self.shrapnels.append(shrapnel)
            self.detonate = False

    def shrapnel_move(self):
        for each in self.shrapnels:
            each.forward(1.5)
            if each.xcor() > 320:
                self.removeshrapnel(each)

    def removeshrapnel(self, each):
        self.shrapnels.remove(each)
        each.hideturtle()
        each.clear()

    def bomb_reset(self):
        for shrapnel in self.shrapnels[:]:
            self.removeshrapnel(shrapnel)
        self.detonate = True
