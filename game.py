#import library
import pygame,pyttsx3,time,random

from pygame.locals import *


pygame.mixer.pre_init(44100,16,2,4096)
#initialization
pygame.init()

width = 1352
height = 688

#color
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
gray=(50, 50, 50)
red=(0, 51, 51)
yellow=(255, 255, 0)


#display Screen
gameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#game title
pygame.display.set_caption('Python Game Project')
#used for frames per second
clock = pygame.time.Clock()


#image display
img = pygame.image.load('1.jpg')

def wel(x,y):
    gameDisplay.blit(img, (x,y))

img1 = pygame.image.load('3.jpg')

def wel1(x,y):
    gameDisplay.blit(img1, (x,y))

img2 = pygame.image.load('2.png')

def wel2(x,y):
    gameDisplay.blit(img2, (x,y))

img3 = pygame.image.load('2.jpg')

def wel3(x,y):
    gameDisplay.blit(img3, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf, TextRect)



def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action=="play":
                gameloop()
            if action == 'Next':
                gameloop1()
            if action == "quit":
                quitgame()
            if action == "Esc":
                main_func()
            if action == "start":
                music2()
                import main

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

#initaialize audio
def audio():
    engine = pyttsx3.init()
    engine.say("Welcome to the Game")
    engine.say("Need For Speed")
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 10.0)
    engine.runAndWait()
    engine.stop()
def audio1():

    engine = pyttsx3.init()
    engine.say('controls')
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 100.0)
    engine.runAndWait()
    engine.stop()


#initialize music
def music():
     pygame.mixer_music.load("1.mp3")
     pygame.mixer_music.play(0)


def music1():
    pygame.mixer_music.load("2.mp3")
    pygame.mixer_music.play(0)

def music2():
    pygame.mixer_music.load("3.mp3")
    pygame.mixer_music.play(0)

def music3():
    pygame.mixer_music.load("4.mp3")
    pygame.mixer_music.play(0)



def gameloop():
   music1()
   crashed = False
   gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
   # game title
   pygame.display.set_caption('Python Game Project')
   clock = pygame.time.Clock()
   while not crashed:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

           gameDisplay.fill(white)
           wel1(0,0)
       button("<-Esc", 30, 550, 150, 50, red, black, action="Esc")
       button("Play->", 1200, 550, 150, 50, red, black, action="Next")
       pygame.display.update()
       clock.tick(60)
       font = pygame.font.Font('freesansbold.ttf', 32)

       text = font.render('Controls', True, green, blue)
       text1 = font.render('up key :- Acceleration', True, green, blue)
       text2 = font.render('down key :- Reverse or Brake', True, green, blue)
       text3 = font.render('right key :- right turn', True, green, blue)
       text4 = font.render('left key :- left turn', True, green, blue)

       textRect = text.get_rect()
       textRect1 = text.get_rect()
       textRect2 = text.get_rect()
       textRect3 = text.get_rect()
       textRect4 = text.get_rect()
       textRect.center = (width // 2, height // 4)
       textRect1.center = (width //2.5, height // 3)
       textRect2.center = (width // 2.5, height // 2.5)
       textRect3.center = (width // 2.5, height // 2.1)
       textRect4.center = (width // 2.5, height // 1.8)


       gameDisplay.blit(text, textRect)
       gameDisplay.blit(text1, textRect1)
       gameDisplay.blit(text2, textRect2)
       gameDisplay.blit(text3, textRect3)
       gameDisplay.blit(text4, textRect4)



def gameloop1():
   music3()
   crashed = False
   gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
   # game title
   pygame.display.set_caption('Python Game Project')
   clock = pygame.time.Clock()
   while not crashed:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

           gameDisplay.fill(white)
           wel3(0,0)
       button("<-Esc", 30, 550, 150, 50, red, black, action="Esc")
       button("Play->", 1200, 550, 150, 50, red, black, action="start")
       pygame.display.update()
       clock.tick(60)
       font = pygame.font.Font('freesansbold.ttf', 32)

       text = font.render('Instructions', True, green, blue)
       text1 = font.render('TRY THE TRAIL MAP', True, green, blue)


       textRect = text.get_rect()
       textRect1 = text.get_rect()
       textRect.center = (width // 2, height // 4)
       textRect1.center = (width // 2, height // 3)
       gameDisplay.blit(text, textRect)
       gameDisplay.blit(text1, textRect1)






#main file
def main_func():
    audio()
    music()

    crashed = False

    while not crashed:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

        gameDisplay.fill(white)
        wel(0,0)

        largeText = pygame.font.SysFont("comicsansms", 75)
        TextSurf, TextRect = text_objects("", largeText)
        TextRect.center = ((width / 2), (height / 5))
        gameDisplay.blit(TextSurf, TextRect)
        button("Play->", 1200, 550, 150, 50, red, black, action="play")
        button("<-Quit", 30, 550, 150, 50, red, black,action="quit")

        pygame.display.update()
        clock.tick(60)

#initialize the game

main_func()
gameloop()

#will exit python and the application
pygame.quit()
quit()

