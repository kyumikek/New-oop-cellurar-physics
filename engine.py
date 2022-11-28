import pygame
import random
color = ["black","yellow","gray","blue","red","brown"]
class engine:
    board = []
    data = []
    updateTime = 0
    
    def setup(screen):
        engine.screen = screen
        for x in range(int(600/25)):
            for y in range(int(800/25)):
                k = object(x*25,y*25,0)
    async def asyncUpdate():
        for i in engine.board:
            i.update()
    def Update():
        for i in engine.board:
            i.update()
    def set(x,y,type,change):
        if([x,y,change] in engine.data):
            bindex = engine.data.index([x,y,change])
            engine.data[bindex][2] = type
    def find(x,y,type):
        if([x,y,type] in engine.data):
            bindex = engine.data.index([x,y,type])
            return [bindex, True]
        return [0, False]
class object:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        self.id = len(engine.board)
        engine.board.append(self)
        engine.data.append([self.x,self.y,self.type])
    def find(self,x,y,type):
        if([self.x+x,self.y+y,type] in engine.data):
            bindex = engine.data.index([self.x+x,self.y+y,type])
            engine.data[bindex][2] = self.type
            self.type = 0
            engine.data[self.id][2] = self.type
            return True
        return False
    def replace(self,x,y,type):
        if([self.x+x,self.y+y,type] in engine.data):
            bindex = engine.data.index([self.x+x,self.y+y,type])
            engine.data[bindex][2] = self.type
    def update(self):
        pygame.draw.rect(engine.screen,color[self.type],pygame.Rect(self.x,self.y,25,25))
        self.type = engine.data[self.id][2]
        
        r = 1
        match self.type:
            case 1:
                r = 1
                if([self.x,self.y+25,3] in engine.data):
                    bindex = engine.data.index([self.x,self.y+25,3])
                    self.type = engine.data[bindex][2]
                    engine.data[bindex][2] = 1
            case 2:
                r = -1
                goto = random.randint(-1,1)
                self.find(25*goto,0,0)
            case 3:
                goto = random.randint(-1,1)
                self.find(25*goto,0,0)
                self.find(0,25,4)
                self.find(0,-25,4)
                self.find(25,25,4)
                self.find(-25,-25,4)
                self.find(-25,25,4)
                self.find(25,-25,4)
            
        if(self.type!=5 and self.type!=4):
            up = self.find(0,25*r,0)
            if(up==False):
                right = self.find(-25,25*r,0)
                if(right==False):
                    self.find(25,25*r,0)
        
