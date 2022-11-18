import sys
import pygame
screen = pygame.display.set_mode((600,800))
board = []
data = []
color = ["black","yellow","gray"]

class object:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        self.id = len(board)
        board.append(self)
        data.append([self.x,self.y,self.type])
    def find(self,x,y,type):
        if([self.x+x,self.y+y,type] in data):
            bindex = data.index([self.x+x,self.y+y,0])
            data[bindex][2] = self.type
            self.type = 0
            data[self.id][2] = self.type
            return True
        return False
    def update(self):
        self.type = data[self.id][2]
        
        r = 1
        match self.type:
            case 1:
                r = 1
            case 2:
                r = -1 
        up = self.find(0,25*r,0)
        if(up==False):
            right = self.find(-25,25*r,0)
            if(right==False):
                self.find(25,25*r,0)
        pygame.draw.rect(screen,color[self.type],pygame.Rect(self.x,self.y,25,25))
for x in range(int(600/25)):
    for y in range(int(800/25)):
        k = object(x*25,y*25,0)
wait = 0
waitTime = 0
#clock = pygame.time.Clock()
while True:
    click = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    mx = int(mx/25)*25
    my = int(my/25)*25
    #clock.tick()
    #print (clock.get_fps())
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()
    if(click[0] and wait==waitTime):
        if([mx,my,0] in data):
            bindex = data.index([mx,my,0])
            data[bindex][2] = 1
        wait = 0
    if(wait<waitTime):
        wait += 1
    for i in board:
        i.update()
    pygame.display.flip()
