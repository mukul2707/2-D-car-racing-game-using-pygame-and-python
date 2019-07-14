import pygame, time, random
from pygame import  *


#Initialization
pygame.init()
width = 1366
height = 768

#Color
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

#Display Screen
gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Need For Speed")
clock = pygame.time.Clock()


#Main Loop
def main_loop():
    import track

    crashed =False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(200)


#run functions

main_loop()
pygame.quit()
quit()