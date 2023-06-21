from .engine import *

class controller:
    def __init__(self,x,y,speed,mass):
        self.x = x
        self.y = y
        self.speed = speed
        self.mass = mass
        self.y_velocity = 0
    def update(self):
        self.gx = int(self.x/25)*25
        self.gy = int(self.y/25)*25
        pressed_keys = pygame.key.get_pressed()
        
        
        bindex = engine.find(self.gx,self.gy+25,0)
        if(bindex[1]): self.y_velocity += self.mass
        else:
            self.y_velocity = 0
            if(pressed_keys[pygame.K_w]): 
                bindex = engine.find(self.gx,self.gy-25,0)
                if(bindex[1]): self.y -= 125
        bindex = engine.find(self.gx,self.gy,0)
        if(bindex[1]==False): self.y -= 25
        self.y += self.y_velocity
        if(pressed_keys[pygame.K_a]): 
            bindex = engine.find(self.gx-25,self.gy,0)
            if(bindex[1]): self.x -= self.speed 
        elif(pressed_keys[pygame.K_d]): 
            bindex = engine.find(self.gx+25,self.gy,0)
            if(bindex[1]): self.x += self.speed 
        bindex = engine.find(self.gx,self.gy+25,3)
        if(bindex[1]): self.y += 25