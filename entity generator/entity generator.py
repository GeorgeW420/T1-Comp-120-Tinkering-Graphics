import random
import pygame
import time
pygame.init()
main_window = pygame.display.set_mode((800, 600))
running = True
array_of_images = ["enemy one.png" ,"enemy two.gif","enemy three.png"]
x = random.randint(200, 300)
y = random.randint(200, 300)
random_image = random.randint(0, 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = random.randint(100, 300)
    y = random.randint(100, 300)
    random_image = random.randint(0, 2)
    surface = pygame.image.load(array_of_images[random_image])
    main_window.blit(surface, (x, y))
    pygame.display.update()
    time.sleep(1)
pygame.quit()
