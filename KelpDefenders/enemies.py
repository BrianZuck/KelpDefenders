from turtle import RawTurtle
import random


SPEED = 1.15

class Enemies:
    def __init__(self, screen, window):
        self.screen = screen
        self.window = window
        self.enemy_list = []
        self.move_speed = SPEED
        self.spawned_count = 0

    def create_enemy(self, round):
        if self.spawned_count < round * 10:
            dice = random.randint(1,max(16 - round,5))
            if dice == 2 or dice == 3:
                new_enemy = RawTurtle(self.screen)
                new_enemy.shape("turtle")
                new_enemy.setheading(180)
                new_enemy.penup()
                new_enemy.color("red")
                self.gotostart(new_enemy)
                self.enemy_list.append(new_enemy)
                self.spawned_count += 1
        else:
            return False

    def gotostart(self,enemy):
        random_y = random.randint(-300,300)
        enemy.goto(300,random_y)

    def moving(self):
        for enemy in self.enemy_list:
            enemy.forward(self.move_speed)

    def level_up(self):
        self.move_speed += .5

    def remove_enemy(self, enemy):
        self.enemy_list.remove(enemy)
        enemy.hideturtle()
        enemy.clear()


