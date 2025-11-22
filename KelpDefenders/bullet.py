from turtle import RawTurtle
import time
BULLET_SPEED = 30
FONT = ("Courier", 14, "normal")


class Bullet:
    def __init__(self, screen):
        self.screen = screen
        self.bullets = []
        self.maxbullets = 0
        self.upgrades = 1
        self.last_shot_time = 0
        self.counter_turtle = RawTurtle(self.screen)
        self.counter_turtle.hideturtle()
        self.counter_turtle.penup()
        self.cost = 500

    def shoot(self, player, gaming):
        if not gaming:
            return
        current_time = time.time()
        if current_time - self.last_shot_time < .30 or self.maxbullets <= 0:
            return
        self.last_shot_time = current_time
        angles = [0]
        if self.upgrades >= 2:
            angles.append(45)
        if self.upgrades >= 3:
            angles.append(315)
        for angle in angles:
            bullet = RawTurtle(self.screen)
            bullet.hideturtle()
            bullet.shape("circle")
            bullet.shapesize(stretch_wid=.4, stretch_len=.4)
            bullet.color("gray")
            bullet.penup()
            bullet.goto(player.xcor() + 6, player.ycor())
            bullet.setheading(angle)
            bullet.showturtle()
            self.bullets.append(bullet)
        self.maxbullets -= 1
        self.update_counter()


    def move_bullet(self):
        for bullet in self.bullets:
            bullet.forward(BULLET_SPEED)
            if bullet.xcor() > 320:
                self.remove_bullet(bullet)

    def max_bullet_count(self,round, remaining = 0):
        self.maxbullets = round * 15 + remaining
        self.update_counter()

    def remove_bullet(self,bullet):
        self.bullets.remove(bullet)
        bullet.hideturtle()
        bullet.clear()

    def update_counter(self):
        self.counter_turtle.clear()  # clear old text
        self.counter_turtle.goto(-265, 232)
        self.counter_turtle.write(f"Bullets remaining: {self.maxbullets}", align="left", font=FONT)

    def bullet_upgrade_press(self, scoreboard):
        if scoreboard.money >= self.cost and self.upgrades <= 3:
            self.upgrades += 1
            scoreboard.money -= self.cost
            scoreboard.update_scoreboard()
