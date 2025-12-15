from turtle import RawTurtle

BALLOON_IMAGE = 'balloongiphy (1).gif'
STARTING_POS = [(-130, 130), (-130, -130), (130, -130), (130, 130)]


class Balloon(RawTurtle):
    def __init__(self, screen):
        super().__init__(screen)
        screen.register_shape(BALLOON_IMAGE)
        self.penup()
        self.hideturtle()
        self.shape(BALLOON_IMAGE)
        self.shown = False


    def show_balloons(self):
        if self.shown == False:
            for position in STARTING_POS:
                self.goto(position)
                self.stamp()
        self.shown = True

    def balloon_reset(self):
        self.clearstamps(4)
        self.shown = False








