import pygame
import random
pygame.init()

width = 500
height = 500
size = (width, height)
#This is for the size of the map
Background = pygame.image.load('Blue.jpeg')
Platform = pygame.image.load('Platform.Jpg')
Shrine = pygame.image.load('Green.Jpeg')
#files for Jpegs
tile = 64
backx = 0
backy = 0

first = 2

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platform level generation")
platforms = []
#set caption for level name


def setupbackground():
    global backx
    global backy

    while backx <= width:
        screen.blit(Background, (backx, backy))
        pygame.display.update()
        backx = backx + tile
    if backy <= height:
        backy = backy + tile
        backx = 0
        setupbackground()
    else:
        pass

def setupplatform():
    global tile
    global width
    global height
    global backx
    global backy
    global first

    backx = 0
    while backx < width + 64:
        screen.blit(Platform, (backx, backy - tile))
        backx = backx + tile

    randomplat()

def randomplat():
    global backx
    global backy
    global platforms

    backx = backx - 64
    backy = backy - 64

    platformx = random.randrange(0, backx, 64)
    platformy = random.randrange(0, backy, 64)
    screen.blit(Platform, (platformx, platformy))
    screen.blit(Platform, (platformx - 64, platformy))
    screen.blit(Platform, (platformx + 64, platformy))
    list = (platformx, platformy)
    platforms.append(list)

def randomshrine():
    global platforms

    choice = random.randint(0, 5)
    if choice == 1:
        screen.blit(Shrine, (platforms[1]))
    else:
        pass

## this is the main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while first > 0:
        setupbackground()
        setupplatform()
        first = first - 1






pygame.quit()
#end of game
