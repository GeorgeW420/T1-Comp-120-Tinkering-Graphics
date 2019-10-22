import random
import pygame
import time
pygame.init()
main_window = pygame.display.set_mode((800, 600))
running = True
array_of_body = ["body1.png" ,"body2.png","body3.png"]
array_of_heads =["head4.png" , "head5.png", "head6.png"]
array_of_left_arm = ["larm1.png", "larm2.png", "larm3.png"]
array_of_right_arm = ["rarm1.png", "rarm2.png", "rarm3.png"]
array_of_legs = ["legs1.png", "legs2.png" , "legs4.png"]
x = random.randint(200, 300)
y = random.randint(200, 300)
head = random.randint(0, 2)
body = random.randint(0, 2)
left_arm = random.randint(0, 2)
right_arm = random.randint(0, 2)
legs = random.randint(0, 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    random_image_body = random.randint(0, 2)
    random_image_heads = random.randint(0, 2)
    random_image_left_arm = random.randint(0, 2)
    random_image_right_arm = random.randint(0, 2)
    random_image_legs = random.randint(0, 2)

    surface_body = pygame.image.load(array_of_body[random_image_body])
    surface_heads = pygame.image.load(array_of_heads[random_image_heads])
    surface_left_arm = pygame.image.load(array_of_left_arm[random_image_left_arm])
    surface_right_arm = pygame.image.load(array_of_right_arm[random_image_right_arm])
    surface_legs = pygame.image.load(array_of_legs[random_image_legs])
    main_window.blit(surface_body, (10, 10))
    main_window.blit(surface_heads, (20, 20))
    main_window.blit(surface_left_arm, (30, 30))
    main_window.blit(surface_right_arm, (40, 40))
    main_window.blit(surface_legs, (50, 50))
    pygame.display.update()
pygame.quit()
