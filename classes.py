import pygame
pygame.init()

#temporary values, to be changed later
brakespeed = 0.5
maxspeed = 5

class player():

    def __init__(self):
        #initialize all variables

        self.x = 0.0
        self.y = 0.0
        self.h = 25
        self.w = 25
        self.speedx = 0.0
        self.speedy = 0.0
        self.health = 100.0
        self.armour = 0.0

        self.powerup1 = False
        self.powerup2 = False
        self.powerup3 = False

        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

    def move(self,direction):
        #set initial speed according to direction

        if direction == 'up':
            self.speedy = -maxspeed
        elif direction == 'down':
            self.speedy = maxspeed
        elif direction == 'left':
            self.speedx = -maxspeed
        elif direction == 'right':
            self.speedx = maxspeed     

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
    

class line():

    def __init__(self,x1,y1,x2,y2):

        self.name = 'line'
        self.id = 2

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.slope = 0.0
        self.length = 0.0
        self.is_vertical = False
        self.width = 1
        self.color = (0,0,0)

class wall():

    def __init__(self,x,y):
        #initialize all variables

        self.name = 'wall'
        self.id = 1

        self.x = x
        self.y = y
        self.h = 30
        self.w = 30

        self.can_collide = True

        self.image = pygame.image.load('images/wall.png')
        self.image = pygame.transform.scale(self.image, (self.w, self.h))


class door():

    def __init__(self,x,y):
        #initialize all variables

        self.name = 'door'
        self.id = 3

        self.x = x
        self.y = y
        self.h = 30
        self.w = 30

        self.can_collide = True

        self.image = pygame.image.load('images/door.png')
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        

class gamemap():

    def __init__(self,dw,dh):
        #initialize all variables

        self.mapx = 0.1
        self.mapy = 0.1
        self.mapspeedx = 0
        self.mapspeedy = 0

        self.redx1 = 100
        self.redy1 = 100
        self.redx2 = dw - 100
        self.redy2 = dh - 100

        self.map_edge_x = 2200
        self.map_edge_y = 2200

    def inertia(self):
        #same as player inertia
        if self.mapspeedx > 0:
            self.mapspeedx = (self.mapspeedx*1000 - brakespeed*1000)/1000
        elif self.mapspeedx < 0:
            self.mapspeedx = (self.mapspeedx*1000 + brakespeed*1000)/1000

        if self.mapspeedy > 0:
            self.mapspeedy = (self.mapspeedy*1000 - brakespeed*1000)/1000
        elif self.mapspeedy < 0:
            self.mapspeedy = (self.mapspeedy*1000 + brakespeed*1000)/1000

        self.mapx += self.mapspeedx
        self.mapy += self.mapspeedy


class point():
    #temp class
    def __init__(self,x,y):

        self.x = x
        self.y = y