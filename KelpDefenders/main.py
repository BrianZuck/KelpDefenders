from tkinter import *
from turtle import TurtleScreen
from Player import Player
from enemies import Enemies
from bullet import Bullet
from kelp import Kelp
from balloon import Balloon
from bomb import Bomb
from scoreboard import Scoreboard



def start_game():
    global gaming, player, enemy, bullet, scoreboard, bomb, balloon, instruction_label
    gaming = True
    canvas.delete(instruction_label)
    start_button.grid_remove()
    kelp = Kelp(screen)
    bomb = Bomb(screen)
    player = Player(screen)
    enemy = Enemies(screen, window)
    bullet = Bullet(screen)
    balloon = Balloon(screen)
    scoreboard = Scoreboard(screen)
    bullet.max_bullet_count(scoreboard.level)
    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_down, "Down")
    screen.onkey(lambda: bullet.shoot(player, gaming), "space")
    window.after(20, game_loop)


def bombing():
    screen.onclick(lambda x, y: bomb.bomb_move(x, y, bomb_button))
    bomb_button.grid_remove()

def reset_game():
    global gaming
    gaming = True
    reset_button.grid_remove()
    bomb.bomb_reset()
    enemy.enemy_reset()
    scoreboard.score_reset()
    bullet.bullet_reset()
    balloon.balloon_reset()
    player.gotostart()
    screen.update()
    window.after(20, game_loop)

window = Tk()
window.title("Kelp Defenders")
window.config(padx=150, pady=50, bg = '#ADD8E6')

canvas = Canvas(window, width=600, height=600, bg = '#ADD8E6', highlightthickness=2, highlightbackground='#000000')
canvas.grid(column=1, row=2, columnspan=2)

screen = TurtleScreen(canvas)
screen.tracer(0)
screen.bgcolor('#ADD8E6')


start_button = Button(
    text="Start",
    command= start_game,
    width=10,
    height=3,
    font=("Courier", 12, "bold")
)

start_button.grid(column=1, row=1, padx=10, pady=10)

reset_button = Button(
    text="Reset",
    command= reset_game,
    width=10,
    height=3,
    font=("Courier", 12, "bold")
)


exit_button = Button(
    text="Exit",
    command=window.destroy,
    width=10,
    height=3,
    font=("Courier", 12, "bold")
)
exit_button.grid(column=2, row=1, padx=10, pady=10)


upgrade_button = Button(
    text="Upgrade",
    command=lambda: bullet.bullet_upgrade_press(scoreboard),
    width=10,
    height=3,
    font=("Courier", 12, "bold")
)

bomb_button = Button(
    text="Bomb",
    command= bombing,
    width=10,
    height=3,
    font=("Courier", 12, "bold")
)



title_label = Label(window, text="Kelp Defenders", font=("Courier", 25, "bold underline"), fg="#5CDA5C", bg = '#ADD8E6')
title_label.grid(column=1, row=0, columnspan=2)


instruction_label = canvas.create_text(0, 0,
    text="Use ↑ ↓ to Move | Space to Shoot\n"
         "   Upgrade appears at the top\n"
         "    Bomb unlocked in Round 3",
    fill="#1f3a4d",
    font=("Courier", 14, "bold")
)

#### GAME CODE ####

gaming = False

def game_loop():
    global gaming

    if scoreboard.money >= bullet.cost * bullet.upgrades and bullet.upgrades <= 2:
        upgrade_button.grid(column=1, row=1)
    else:
        upgrade_button.grid_remove()

    if scoreboard.level == 3 and bomb.detonate:
        bomb_button.grid(column=2, row=3)

    if not bomb.detonate:
        screen.onclick(None)

    screen.update()
    enemy.moving()
    bullet.move_bullet()
    bomb.shrapnel_move()
    enemy.create_enemy(scoreboard.level)

    for e in enemy.enemy_list[:]:
        if int(e.xcor()) < int(player.xcor()):
            scoreboard.game_over()
            upgrade_button.grid_remove()
            gaming = False
            reset_button.grid(column=1, row=1, padx=10, pady=10)
            return

        for b in bullet.bullets[:]:
            if e.distance(b) < 18:
                enemy.remove_enemy(e)
                bullet.remove_bullet(b)
                scoreboard.add_bank()
                scoreboard.increase_kill()
                break

        for s in bomb.shrapnels[:]:
            if e.distance(s) < 18:
                enemy.remove_enemy(e)
                bomb.removeshrapnel(s)
                scoreboard.add_bank()
                scoreboard.increase_kill()
                break

    if len(enemy.enemy_list) <= 0 and enemy.create_enemy(scoreboard.level) is False:
        enemy.spawned_count = 0
        remaining_bullet = bullet.maxbullets
        scoreboard.increase_level()
        bullet.max_bullet_count(scoreboard.level, remaining_bullet)

    player.bounds()

    if scoreboard.level > 3:
        bomb_button.grid_remove()
        bullet.bullet_reset()
        screen.update()
        scoreboard.winner()
        balloon.show_balloons()
        upgrade_button.grid_remove()
        gaming = False
        reset_button.grid(column=1, row=1, padx=10, pady=10)
        return

    if gaming:
        window.after(16, game_loop)


window.mainloop()
