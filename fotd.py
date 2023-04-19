import random
import pygame
import pgzrun
import pgzero

WIDTH = 1920
HEIGHT = 1080

pygame.mixer.init(22100, -16, 2, 64)

sounds.music.play(-1)

BACKGROUND_IMAGE = "start"
IMG_PREFIX = "player"
direction = "right"
image_number = "1"

player = Actor(IMG_PREFIX + ".right.1")
player.pos = 960, 540

direction = "right"
skee = []
skeletonnum = 4

bull = []
bulletnum = 4

swing = 1
bos = Actor("gray.left." + str(swing))
bos.pos = 960, 540
b = False

bhealth = 200
health = 100

roundn = 1
ran = 1

mousedown = False

timer = 0
timerb = 0
timerb2 = 0

randomlow = 500
randomhigh = 750
randlowb = 10
randhighb = 45

randno = random.randint(randomlow,randomhigh)
randnob = random.randint(randlowb,randhighb)

health = 100

ll = 800 - bhealth * 4
lr = 1024 + (bhealth * 4)

healthbar = Rect(1590, 980, 266, 56)
healthplat = Rect(1856-(abs(100-health)*2.66), 980, 266, 56)
bhealthplat = Rect(96, 10, 1728, 100)
bcoverl = Rect(96, 25, (ll), 60)
bcoverr = Rect((lr), 25, 800, 60)

playr = Rect(705, 585, 510, 110)
play = Rect(710, 590, 500, 100)
helpra = Rect(705, 785, 510, 110)
helpr = Rect(710, 790, 500, 100)
playar = Rect(705, 835, 510, 110)
playa = Rect(710, 840, 500, 100)
back = Rect(705, 900, 510, 110)
backa = Rect(710, 905, 500, 100)

s = 2
sb = 2

fired = False

col = 21, 21, 22
bcol = 36, 104, 75

game = 1


def on_mouse_down(button):
    global mousedown
    sounds.sword.play()
    if button == mouse.LEFT:
        mousedown = True


def skeletonadder():
    global skee, skeletonnum, bull, bullnum
    bullnum = 0
    skeenum = 0
    skee = []
    bull = []
    for i in range(skeletonnum):
        num = random.randint(1,2)
        if num == 1:
            direction = "left"
        else:
            direction = "right"
        skee.append(Actor("skeleton." + str(direction)))
        bull.append(Actor("bullet"))
        positionx = random.randint(490, 1450)
        positiony = random.randint(250, 800)
        skee[skeenum].pos = positionx, positiony
        bull[bullnum].pos = positionx, positiony
        skeenum += 1
        bullnum += 1


def shoot():
    global s, health, timer, randno, fired, dire, bull
    if not fired:
        dire = player.pos
        fired = True
        for skele in skee:
            sounds.gun.play()
            animate(bull[skee.index(skele)], pos = dire, duration = 0.5, tween = 'accelerate')
    timer = 0
    randno = random.randint(randomlow,randomhigh)
    for bulle in bull:
        if (player.colliderect(bulle)):
            health -= 5
            s = 2
            fired = False
        if bulle.pos == dire:
            s = 2
            fired = False


def boss():
    global b, sb, health, timerb, randnob, randlowb, randhighb, mousedown, bhealth, swing, bos, timerb2, randhighb2, randlowb2, randnob2, game
    if bhealth > 0:
        b = True
        if (player.colliderect(bos)):
            if sb == 1:
                sounds.swoosh.play()
                health -= 5
                timerb = 0
                randnob = random.randint(randlowb,randhighb)
                sb = 2
            else:
                timerb += 1
                if timerb == randnob:
                    sb = 1
            if mousedown:
                bhealth -= 5
                mousedown = False
        else:
            timerb = 0
        if player.x > bos.x:
            bos.image = "gray.right." + str(swing)
        else:
            bos.image = "gray.left." + str(swing)
        animate(bos, pos=(player.x, player.y), duration = 2)
    else:
        b = False
        mousedown = False
        game = 4

def varset():
    global IMG_PREFIX, ll, lr, bcoverl, bcoverr, direction, image_number, player, skee, skeletonnum, s, sb, fired, col, bcol, bull, bulletnum, swing, bos, b, bhealth, health, bhealthplat, playr, play, playa, playar, healthbar, healthplat, roundn, ran, mousedown, timer, timerb, timerb2, randomlow, randomhigh, randlowb, randhighb, randno, randnob
    IMG_PREFIX = "player"
    direction = "right"
    image_number = "1"
    player = Actor(IMG_PREFIX + ".right.1")
    player.pos = 960, 540
    direction = "right"
    skee = []
    skeletonnum = 4
    bull = []
    bulletnum = 4
    swing = 1
    bos = Actor("gray.left." + str(swing))
    bos.pos = 960, 540
    b = False
    bhealth = 200
    health = 100
    roundn = 1
    ran = 1
    mousedown = False
    timer = 0
    timerb = 0
    timerb2 = 0
    randomlow = 500
    randomhigh = 750
    randlowb = 10
    randhighb = 45
    randno = random.randint(randomlow,randomhigh)
    randnob = random.randint(randlowb,randhighb)
    health = 100
    ll = 800 - bhealth * 4
    lr = 1024 + (bhealth * 4)
    healthbar = Rect(1590, 980, 266, 56)
    healthplat = Rect(1856-(abs(100-health)*2.66), 980, 266, 56)
    bhealthplat = Rect(96, 10, 1728, 100)
    bcoverl = Rect(96, 25, (ll), 60)
    bcoverr = Rect((lr), 25, 800, 60)
    playr = Rect(705, 585, 510, 110)
    play = Rect(710, 590, 500, 100)
    helpra = Rect(705, 785, 510, 110)
    helpr = Rect(710, 790, 500, 100)
    playar = Rect(705, 835, 510, 110)
    playa = Rect(710, 840, 500, 100)
    back = Rect(705, 900, 510, 110)
    backa = Rect(710, 905, 500, 100)
    s = 2
    sb = 2
    fired = False
    col = 21, 21, 22
    bcol = 36, 104, 75

def draw():
    if game == 1:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        screen.draw.filled_rect(playr,col)
        screen.draw.filled_rect(play,bcol)
        screen.draw.text("Play", center = (960, 640), fontname="windlass", fontsize=70)
        screen.draw.filled_rect(helpra,col)
        screen.draw.filled_rect(helpr,bcol)
        screen.draw.text("How to Play", center = (960, 840), fontname="windlass", fontsize=70)
    if game == 2:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        screen.blit('health', healthbar)
        screen.draw.filled_rect(healthplat,col)
        for skele in skee:
            if not(skele == 0):
                skele.draw()
                for bulle in bull:
                    bulle.draw()
        if b == True:
            bos.draw()
            screen.blit('bhealth', bhealthplat)
            screen.draw.filled_rect(bcoverl,col)
            screen.draw.filled_rect(bcoverr,col)
        player.draw()
    if game == 3:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        screen.draw.filled_rect(playar,col)
        screen.draw.filled_rect(playa,bcol)
        screen.draw.text("Play Again", center = (960, 890), fontname="windlass", fontsize=70)
        screen.draw.text("You have been dragged to depths of the Earth by Lord Graymarrow.", center = (960, 640), fontname="windlass", fontsize=40)
        screen.draw.text("Better Luck Next Time!", center = (960, 740), fontname="windlass", fontsize=70)
    if game == 4:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        screen.draw.filled_rect(playar,col)
        screen.draw.filled_rect(playa,bcol)
        screen.draw.text("Play Again", center = (960, 890), fontname="windlass", fontsize=70)
        screen.draw.text("You have slayed Lord Graymarrow and his minions.", center = (960, 640), fontname="windlass", fontsize=40)
        screen.draw.text("Enjoy Your Glory Amongst the Sea of Thieves!", center = (960, 740), fontname="windlass", fontsize=70)
    if game == 5:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        screen.draw.filled_rect(back,col)
        screen.draw.filled_rect(backa,bcol)
        screen.draw.text("Back", center = (960, 955), fontname="windlass", fontsize=70)
        screen.draw.text("10 Round Game - 9 Rounds vs. Skeletons - Kill all of the Skellies to Move On, Followed by a Boss Round", center = (960, 520), fontname="windlass", fontsize=30)
        screen.draw.text("WASD to Move Around the Screen and Escape Key to Quit Game", center = (960, 570), fontname="windlass", fontsize=30)
        screen.draw.text("Hover Over the Skeletons and Left Click to Kill/Do Damage (Boss)", center = (960, 620), fontname="windlass", fontsize=30)
        screen.draw.text("Your Health is Displayed in the Bottom Right and the Boss' on the Top", center = (960, 670), fontname="windlass", fontsize=30)
        screen.draw.text("PAY ATTENTION TO THESE!", center = (960, 720), fontname="windlass", fontsize=30)
        screen.draw.text("The Skeletons will Shoot at You Lowering your Heath", center = (960, 770), fontname="windlass", fontsize=30)
        screen.draw.text("The Longer Time you Spend on Top of the Boss the more Health taken from You", center = (960, 820), fontname="windlass", fontsize=30)
        screen.draw.text("FINALLY, PIRATE LORD'S WILLING YOU COME OUT ALIVE!", center = (960, 870), fontname="windlass", fontsize=30)


def update():
    global ll, bcoverl, bcoverr, lr, timer, game, randno, direction, skeletonnum, ran, roundn, mousedown, s, bull, healthplat, health, xpos, BACKGROUND_IMAGE, bhealth, bhealthplat
    if keyboard.escape:
        quit()
    if game == 1:
        if (playr.collidepoint(pygame.mouse.get_pos())) and (mousedown):
            BACKGROUND_IMAGE = "bwip"
            game = 2
            mousedown = False
        if (helpra.collidepoint(pygame.mouse.get_pos())) and (mousedown):
            game = 5
            mousedown = False
    elif game == 2:
        ll = 800 - bhealth * 4
        lr = 1024 + (bhealth * 4)
        bhealthplat = Rect(96, 10, 1728, 100)
        bcoverl = Rect(96, 25, (ll), 60)
        bcoverr = Rect((lr), 25, 800, 60)
        healthplat = Rect(1856-(abs(100-health)*2.66), 980, 266, 56)
        if health > 0:
            if keyboard.w and (player.y > 250):
                if player.y > 40:
                    player.y -= 5
            if keyboard.s and (player.y < 800):
                if player.y < 1040:
                    player.y += 5
            if keyboard.a and (player.x > 490):
                if player.x > 40:
                    player.x -= 5
                    direction = "left"
            if keyboard.d and (player.x < 1450):
                if player.x < 1880:
                    player.x += 5
                    direction = "right"
            image_name = "{}.{}.{}".format(IMG_PREFIX, direction, image_number)
            player.image = image_name
            if ran == 1:
                skeletonadder()
                ran = 0
            for skele in skee:
                if not(skele == 0):
                    if (player.colliderect(skele)) and (mousedown):
                        snum = skee.index(skele)
                        del skee[snum]
                        del bull[snum]
                        skeletonnum -= 1
                        if skeletonnum < 1:
                            roundn += 1
                            if roundn == 2:
                                skeletonnum = (random.randint(3,5))
                                skeletonadder()
                            if roundn == 3:
                                skeletonnum = (random.randint(4,6))
                                skeletonadder()
                            if roundn == 4:
                                skeletonnum = (random.randint(5,7))
                                skeletonadder()
                            if roundn == 5:
                                skeletonnum = (random.randint(5,8))
                                skeletonadder()
                            if roundn == 6:
                                skeletonnum = (random.randint(6,8))
                                skeletonadder()
                            if roundn == 7:
                                skeletonnum = (random.randint(7,9))
                                skeletonadder()
                            if roundn == 8:
                                skeletonnum = (random.randint(8,10))
                                skeletonadder()
                            if roundn == 9:
                                skeletonnum = (random.randint(9,11))
                                skeletonadder()
                if s == 1:
                    shoot()
                else:
                    timer += 1
                    if timer == randno:
                        s = 1
            if roundn == 10:
                boss()
            for skele in skee:
                if player.x > bos.x:
                    skele.image = "skeleton.right"
                else:
                    skele.image = "skeleton.left"
                animate(skele, pos=(player.x, player.y), duration = 7)
                if not s == 1:
                    bull[skee.index(skele)].pos = skele.pos
            mousedown = False
        else:
            game = 3
    elif game == 3:
        BACKGROUND_IMAGE = "start"
        if (playar.collidepoint(pygame.mouse.get_pos())) and (mousedown):
            BACKGROUND_IMAGE = "bwip"
            varset()
            game = 2
            mousedown = False
    elif game == 4:
        BACKGROUND_IMAGE = "start"
        if (playar.collidepoint(pygame.mouse.get_pos())) and (mousedown):
            BACKGROUND_IMAGE = "bwip"
            varset()
            game = 2
            mousedown = False
    elif game == 5:
        BACKGROUND_IMAGE = "start"
        if (back.collidepoint(pygame.mouse.get_pos())) and (mousedown):
            BACKGROUND_IMAGE = "start"
            game = 1
            mousedown = False
    mousedown = False


pgzrun.go()
