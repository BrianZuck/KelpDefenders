from turtle import RawTurtle

KELP_IMAGE = 'giphy-ezgif.com-resize.gif'
STARTING_POS = [(-285, i) for i in range(-280, 281, 40)]


class Kelp(RawTurtle):
    def __init__(self, screen):
        super().__init__(screen)
        screen.register_shape(KELP_IMAGE)
        self.penup()
        self.hideturtle()
        self.shape(KELP_IMAGE)

        for position in STARTING_POS:
            self.goto(position)
            self.stamp()









