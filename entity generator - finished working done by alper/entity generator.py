import random
import pygame
import time# this imports the time for a delay
pygame.init()
main_window = pygame.display.set_mode((1280, 1024))# this is the window size for the generator
running = True# this is for the while loop
array_of_body = ["body1.png" ,"body2.png","body3.png"]# all of these arrays just load the images
array_of_heads =["head1.png" , "head2.png", "head3.png"]
array_of_left_arm = ["larm1.png", "larm2.png", "larm3.png"]
array_of_right_arm = ["rarm1.png", "rarm2.png", "rarm3.png"]
array_of_legs = ["legs1.png", "legs2.png" , "legs3.png"]
x = random.randint(200, 300)#this just spawns the random images in a specific location
y = random.randint(200, 300)
head = random.randint(0, 2)#these code's do the same thing by picking a image in the array at random
body = random.randint(0, 2)
left_arm = random.randint(0, 2)
right_arm = random.randint(0, 2)
legs = random.randint(0, 2)
while running:#this is my while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False#this closes the window automatically
    random_image_body = random.randint(0, 2)#these puts the random image in the scene
    random_image_heads = random.randint(0, 2)
    random_image_left_arm = random.randint(0, 2)
    random_image_right_arm = random.randint(0, 2)
    random_image_legs = random.randint(0, 2)

    surface_body = pygame.image.load(array_of_body[random_image_body])#these load the image in the scene
    surface_heads = pygame.image.load(array_of_heads[random_image_heads])
    surface_left_arm = pygame.image.load(array_of_left_arm[random_image_left_arm])
    surface_right_arm = pygame.image.load(array_of_right_arm[random_image_right_arm])
    surface_legs = pygame.image.load(array_of_legs[random_image_legs])
    main_window.blit(surface_body, (5, 10))#these just to adjust position the images
    main_window.blit(surface_heads, (10, 10))
    main_window.blit(surface_left_arm, (8, 10))
    main_window.blit(surface_right_arm, (8, 9))
    main_window.blit(surface_legs, (5, 12))
    running = False# this is to end the loop so it doesnt spam infinatly
    pygame.display.update()#this updates the screen with the loaded images
    pygame.image.save(main_window, "Monster.png")# this saves the image
    time.sleep(4)#this is just for testing
pygame.quit()#this closes the window
