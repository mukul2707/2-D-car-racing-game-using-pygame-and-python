import pygame, time, random,math
from math import tan, radians, degrees, copysign
from pygame.math import Vector2
from pygame.locals import *
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)
blue = (0, 0, 128)
width = 1366
height = 768




gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Need For Speed")
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf, TextRect)

def crash():
    message_display('You Crashed! Try Again')


def pause():
    pause = True
    crash()
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("<-Esc", 30, 550, 150, 50, green, black, action="esc")
        button("Try Again->", 1200, 550, 150, 50, green, black, action="Try Again")
        pygame.display.update()
        clock.tick(60)






def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action=="Try Again":
                track()
            if action == "esc":
                import game


    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def load_image(x , y, image_name):
    img = pygame.image.load(image_name)
    gameDisplay.blit(img, (x, y))

def track():
    background = pygame.image.load('b1.png')
    carImg = pygame.image.load('2.png')


    backgroundX = 0
    backgroundY = 0

    xpos = 170
    ypos = 100
    keys = [False, False, False, False]
    direction = 0
    forward = 0
    crashed =False

    thing_x = random.randrange(250, 1210)
    thing_y = random.randrange(10, 180)
    thing_x1 = random.randrange(250, 1210)
    thing_y1 = random.randrange(10, 180)
    thing_x = random.randrange(250, 1210)
    thing_y = random.randrange(10, 180)
    thing_x2 = random.randrange(250, 1210)
    thing_y2 = random.randrange(10, 180)
    thing_x3 = random.randrange(250, 1210)
    thing_y3 = random.randrange(10, 180)
    thing_x4 = random.randrange(250, 1210)
    thing_y4 = random.randrange(480, 650)
    thing_x5 = random.randrange(250, 1210)
    thing_y5 = random.randrange(480, 650)
    thing_x6 = random.randrange(250, 1210)
    thing_y6 = random.randrange(480, 650)
    thing_x7 = random.randrange(250, 1210)
    thing_y7 = random.randrange(480, 650)
    thing_x8 = random.randrange(50, 120)
    thing_y8 = random.randrange(50, 200)
    thing_width = 20
    thing_height = 85



    while not crashed:
        clock.tick(200)

        if keys[0] == True:
            direction += 5
        if keys[1] == True:
            direction -= 5
        if keys[2] == True:
            forward -= 1
        if keys[3] == True:
            forward += 1

        movex = math.cos(direction / 57.29) * forward
        movey = math.sin(direction / 57.29) * forward
        backgroundX += movex
        backgroundY -= movey
        xpos-=movex
        ypos+=movey


        playerrot = pygame.transform.rotate(carImg, direction)
        gameDisplay.blit(background, (0, 0))
        load_image(thing_x, thing_y, 'car1.png')
        load_image(thing_x1, thing_y1, 'car3.png')
        load_image(thing_x2, thing_y2, 'car5.png')
        load_image(thing_x3, thing_y3, 'car4.png')
        load_image(thing_x4, thing_y4, 'car51.png')
        load_image(thing_x5, thing_y5, 'car52.png')
        load_image(thing_x6, thing_y6, 'car9.png')
        load_image(thing_x7, thing_y7, 'car53.png')
        load_image(thing_x8, thing_y8, 'car54.png')



        gameDisplay.blit(playerrot, (xpos, ypos))
        if xpos > 1210 or xpos < 90:
            pause()
        if ypos > 610 or ypos < 10:
            pause()





        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    keys[0] = True
                elif event.key == K_RIGHT:
                    keys[1] = True
                elif event.key == K_UP:
                    keys[2] = True
                elif event.key == K_DOWN:
                    keys[3] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[0] = False
                elif event.key == pygame.K_RIGHT:
                    keys[1] = False
                elif event.key == pygame.K_UP:
                    keys[2] = False
                elif event.key == pygame.K_DOWN:
                    keys[3] = False


        pygame.display.update()


        clock.tick(200)


track()
pygame.quit()
quit()

