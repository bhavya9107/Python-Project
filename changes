import pygame
pygame.init()

brakespeed = 0.05

class player():

    def __init__(self):
        #initialize all variables

        self.x = 0.0
        self.y = 0.0
        self.h = 20
        self.w = 20
        self.speedx = 0.0
        self.speedy = 0.0
        self.health = 100.0
        self.armour = 0.0

        self.powerup1 = False
        self.powerup2 = False
        self.powerup3 = False

        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

    def move(self,direction):
        #set initial speed according to direction
		#speedx and speedy changing variables that change position

        if direction == 'up':
            self.speedy = -5

        elif direction == 'down':
            self.speedy = 5

        elif direction == 'left':              #changes
            self.speedx = -5

        elif direction == 'right':
            self.speedx = 5  


    def inertia(self):
        #constantly reduce speed till it is zero for smooth motion
        #brakespeed is low to see the slowing effect

        if self.speedx > 0:
            self.speedx = (self.speedx*1000 - brakespeed*1000)/1000
        elif self.speedx < 0:
            self.speedx = (self.speedx*1000 + brakespeed*1000)/1000

        if self.speedy > 0:
            self.speedy = (self.speedy*1000 - brakespeed*1000)/1000
        elif self.speedy < 0:
            self.speedy = (self.speedy*1000 + brakespeed*1000)/1000

        #always adds speed to x and y coords
        self.x += self.speedx
        self.y += self.speedy

    def shoot():
        pass

    def interact():
        pass


class wall():
    #initialising wall variables

    def __init__(self):
        self.x = 0
        self.y = 0
        self.h = 40
        self.w = 40
        self.collide = False
        self.image = C:\Users\ashok\Desktop\download.jpg
        self.image = pygame.trabsform.scale(self.image, (self.wall_h,self.wall_w))
