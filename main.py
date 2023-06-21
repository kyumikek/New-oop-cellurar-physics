from .engine import *
import sys
import pygame
from .controller import *
screen = pygame.display.set_mode((600,800))
wait = 0
waitTime = 0
engine.setup(screen)
choosen = 0

clock = pygame.time.Clock()
k = controller(0,0,15,5)
while True:
    clock.tick(50)    
    click = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    mx = int(mx/25)*25
    my = int(my/25)*25
    #clock.tick()
    #print (clock.get_fps())
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()
        if(event.type==pygame.KEYDOWN):
            match event.key:
                case pygame.K_0:
                    choosen = 0
                case pygame.K_1:
                    choosen = 1
                case pygame.K_2:
                    choosen = 2
                case pygame.K_3:
                    choosen = 3
                case pygame.K_4:
                    choosen = 4
                case pygame.K_5:
                    choosen = 5
    k.update()
    if(click[0] and wait==waitTime):
        engine.set(mx,my,choosen,0)
        wait = 0
    if(wait<waitTime):
        wait += 1
    engine.Update()
    pygame.draw.rect(screen,"white",pygame.Rect(k.gx,k.gy,25,25))            

    pygame.display.flip()