import pygame
import sys
from classes import *

pygame.init()

#global variables
fps = 60
display_width = 1366
display_height = 768
player1 = player()
map1 = gamemap(display_width,display_height)
objects = [] 
lines = []
mode = ''

#color variables
black = (0,0,0)
white = (255,255,255)
blue=(0,0,255)
red=(255,0,0)

# main pygame variables
gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,50)

def menu():
    pass

def message(msg,color,mesx,mesy):
    
    screen = font.render(msg,True,color)
    gameDisplay.blit(screen,[mesx,mesy])
def gameintro():
    start = True
    load=0
    global mode
    while start:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameexit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    load = 1
                    start = False
                    mode = 'play'
                elif event.key == pygame.K_e:
                    load = 1
                    start = False
                    mode = 'edit'
                                  
                 
         gameDisplay.fill(black)
         if load ==1:
              message('LOADING...',red,500,500)
              pygame.display.update()
         message('WELCOME TO THE BEST GAME EVER',blue,300,500)
         message('PRESS s TO START THE GAME',white,400,700)
            
           
         pygame.display.update()
         clock.tick(60)

def gameinit():
    load_map('level1')           

def gameloop():
   
    quit = False
    
    while quit == False:


        is_O_pressed = False
   	    #events---------------------------------------------------------------------------------------------------
        for event in pygame.event.get():
        
            # event - quit
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:

                #close game if backspace is pressed
                #(made this shortcut as game cannot be closed in full screen)
                if event.key == pygame.K_BACKSPACE:
                    quit = True
                #toggles fulscreen mode when pressing esc
                if event.key == pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_o:
                    is_O_pressed = True
                    
                    

            #used for debugging
            #print event

        #this event runs when any key is pressed
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] == True:
            player1.move('left')
        if pressed_keys[pygame.K_RIGHT] == True:
            player1.move('right')
        if pressed_keys[pygame.K_UP] == True:
            player1.move('up')
        if pressed_keys[pygame.K_DOWN] == True:
            player1.move('down')
        
        
        mcoords = point(pygame.mouse.get_pos()[0] ,pygame.mouse.get_pos()[1] )      


        #logic------------------------------------------------------------------------------------------------------

        is_collided = False
        for obj in objects:
            #check collision with every object on the map
            if collide(player1,obj,map1.mapx,map1.mapy) == True:
                is_collided = True
                if obj.name == 'door':
                    if is_O_pressed == True:
                        obj.can_collide = False
                        is_O_pressed = False
                break
        
            
        
        if is_collided == False:
            #player is not touching anything

            if player1.speedx > 0:
                #player moving towards right

                if player1.x < map1.redx2 :
                    #player is inside red box
                    map1.mapspeedx = 0
                else:
                    #player is outside red box

                    if (-1*map1.mapx) + display_width < map1.map_edge_x:
                        #some portion of map is hidden to the right of the screen
                    
                        map1.mapspeedx = -1*player1.speedx 
                        player1.speedx = 0
                        #move map to left instead of moving player to right and stop the player

                    elif (-1*map1.mapx) + display_width == map1.map_edge_x:
                        #no portion of map left on the right of the screen

                        player1.speedx = -1*map1.mapspeedx
                        map1.mapspeedx = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedx < 0:
                #player moving towards left
               
                if player1.x > map1.redx1 :
                    #player is inside red box
                    map1.mapspeedx = 0
                else:
                    #player is outside red box

                    if map1.mapx < 0:
                        #some portion of map is hidden to the left of the screen
                    
                        map1.mapspeedx = -1*player1.speedx 
                        player1.speedx = 0
                        #move map to right instead of moving player to left and stop the player

                    elif map1.mapx == 0:
                        #no portion of map left on the left of the screen
                        
                        player1.speedx = -1*map1.mapspeedx
                        map1.mapspeedx = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedy > 0:
                #player moving downwards

                if player1.y < map1.redy2 :
                    #player is inside red box
                    map1.mapspeedy = 0
                else:
                    #player is outside red box

                    if (-1*map1.mapy) + display_height < map1.map_edge_y:
                        #some portion of map is hidden below the screen
                    
                        map1.mapspeedy = -1*player1.speedy 
                        player1.speedy = 0
                        #move map upwards instead of moving player downwards and stop the player

                    elif (-1*map1.mapy) + display_height == map1.map_edge_y:
                        #no portion of map left below the screen

                        player1.speedy = -1*map1.mapspeedy
                        map1.mapspeedy = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedy < 0:
                #player moving upwards

                if player1.y > map1.redy1 :
                    #player is inside red box
                    map1.mapspeedy = 0
                else:
                    #player is outside red box

                    if map1.mapy < 0:
                        #some portion of map is hidden above the screen
                    
                        map1.mapspeedy = -1*player1.speedy 
                        player1.speedy = 0
                        #move map downward instead of moving player upward and stop the player

                    elif map1.mapy == 0:
                        #no portion of map left above the screen

                        player1.speedy = -1*map1.mapspeedy
                        map1.mapspeedy = 0
                        #set player speed to reverse of map speed and stop map from moving


        else:
            #player is touching something
            
            
            if player1.speedx != 0:
                #player moving in x axis

                if player1.x <= map1.redx2 or player1.x >= map1.redx1:
                    #player is inside red box
                    player1.speedx *= -0.1 
                    map1.mapspeedx = 0
                else:
                    #player is on red box

                    if ((-1*map1.mapx) + display_width < map1.map_edge_x) or (map1.mapx <0):
                        #map is not scrolled all the way
                    
                        map1.mapspeedx *= -0.1 
                        player1.speedx = 0
                        
                    elif ((-1*map1.mapx) + display_width == map1.map_edge_x) or (map1.mapx == 0):
                        #either of map edge is touching screen edge

                        player1.speedx *= -0.1
                        map1.mapspeedx = 0

            if player1.speedy != 0:
                #player moving in y axis

                if player1.y <= map1.redy2 or player1.y >= map1.redy1 :
                    #player is inside red box
                    player1.speedy *= -0.1
                    map1.mapspeedy = 0
                else:
                    #player is outside red box

                    if ((-1*map1.mapy) + display_height < map1.map_edge_y) or (map1.mapy < 0):
                        #map is not scrolled all the way
                    
                        map1.mapspeedy *= -0.1 
                        player1.speedy = 0
                        
                    elif ((-1*map1.mapy) + display_height == map1.map_edge_y) or (map1.mapy == 0):
                        #either of map edges is touching screen edge

                        player1.speedy *= -0.1
                        map1.mapspeedy = 0
                                               
            player1.inertia()
            map1.inertia()
            player1.speedx = 0
            player1.speedy = 0
            map1.mapspeedx = 0
            map1.mapspeedy = 0

        player1.inertia()
        map1.inertia()

        #update location of lines with map just to check intersection
        for l in lines:
            l.x1 += map1.mapx
            l.y1 += map1.mapy
            l.x2 += map1.mapx
            l.y2 += map1.mapy
        #ipdate location of mouse just for calculations
        #mcoords.x += map1.mapx
        #mcoords.y += map1.mapy


        gameDisplay.fill(white)
        draw_map(map1.mapx,map1.mapy)
        

        #logic for line intersection

        tempx = mcoords.x
        tempy = mcoords.y 
        tempcol = red
   

        final_point = point(0,0)
        intersection_point = point(0,0)
        shortest_len = 100000000000
        
        line1 = line(player1.x + (player1.w/2),player1.y + (player1.h/2) , tempx,tempy)
        line1.length = ((line1.x2-line1.x1)**2 + (line1.y2-line1.y1)**2)**0.5
        line1.color = tempcol

        if line1.x2 != line1.x1:
            line1.slope = (line1.y2 - line1.y1) / (line1.x2 - line1.x1)
        else:
            #slope is infinity
            line1.is_vertical = True
            


        #for i in range(0,20):
        for line2 in lines:
            #line2 = lines[14]
            
            if line1.is_vertical == True and line2.is_vertical == True:
                #either they are the same lines or they are parallel
                continue
                

            elif line1.is_vertical == True and line2.is_vertical == False:
                #     (y-y1) = m2(x-x1) is the equation for line 2
                #      and x = x1 = x2 is the equation for line 1 
                #   =>    y  = m2x - m2x1 + y1
                #   where x is from line 1

                intersection_point.x = line1.x1
                intersection_point.y = (line2.slope*line1.x1) - (line2.slope*line2.x1) + line2.y1
                if intersection_point.y < line1.y1 or intersection_point.y > line1.y2:
                    continue
            
            elif line1.is_vertical == False and line2.is_vertical == True:
                # opposite of above case
            
                intersection_point.x = line2.x1
                intersection_point.y = (line1.slope*line2.x1) - (line1.slope*line1.x1) + line1.y1
                if intersection_point.y < line2.y1 or intersection_point.y > line2.y2:
                    continue

            else:
                
                if line1.slope - line2.slope == 0:
                    #either they are the same line or parallel
                    continue
                    
            
                #both lines have finite slopes
                # for line 1 -> l1y=m1(x-l1x1) + l1y1
                # for line 2 -> l2y=m2(x-l2x1) + l2y1
                # for intersection y of both lines is same 
                #     => l1y = l2y
                #   => m1x - m1.l1x1 + l1y1 = m2x - m2.l2x1 + l2y1
                #   => (m1-m2)x = m1.l1x1 - m2.l2x1 - l1y1 + l2y1
                #   =>        x = (m1.lix1 - m2.l2x1 - liy1 + l2y1) / (m1-m2)
                #putting this value of x in equation for l1y we get y

                intersection_point.x = ((line1.slope*line1.x1) - (line2.slope*line2.x1) - line1.y1 + line2.y1) / (line1.slope - line2.slope)
                intersection_point.y = (line1.slope*intersection_point.x) - (line1.slope*line1.x1) + line1.y1
                #pygame.draw.circle(gameDisplay,black,(int(intersection_point.x),int(intersection_point.y)),3,0)

            p1 = point(line1.x1,line1.y1)
            p2 = point(line1.x2,line1.y2)
            p3 = point(line2.x1,line2.y1)
            p4 = point(line2.x2,line2.y2)
            p = point(intersection_point.x,intersection_point.y)
            #now we have to check if intersection point lies on both line segments or not
            #as the intersection can be found by extending the lines also

            
            if isBetween(p1,p2,p) == True and isBetween(p3,p4,p) == True:
                
                temp_length = ((intersection_point.x-line1.x1)**2 + (intersection_point.y-line1.y1)**2)**0.5
                if temp_length < shortest_len:
                    shortest_len = temp_length
                    final_point.x = intersection_point.x
                    final_point.y = intersection_point.y
            
            
            if line1.length < shortest_len:
                final_point.x = line1.x2
                final_point.y = line1.y2

            pygame.draw.line(gameDisplay,blue,(line2.x1,line2.y1),(line2.x2,line2.y2),2)
            #pygame.draw.circle(gameDisplay,red,(int(final_point.x),int(final_point.y)),3,0)
        pygame.draw.line(gameDisplay,line1.color,(line1.x1,line1.y1),(final_point.x,final_point.y),2)

        #update location of lines back to orignal
        for l in lines:
            l.x1 -= map1.mapx
            l.y1 -= map1.mapy
            l.x2 -= map1.mapx
            l.y2 -= map1.mapy

        #ipdate location of mouse to normal
        #mcoords.x -= map1.mapx
        #mcoords.y -= map1.mapy

        
	    #map draw-----------------------------------------------------------------------------------------------------
        
        pygame.display.update()
        clock.tick(fps)





def gameexit():
    #runs before closing the window
    pygame.quit()
    quit()


def draw(obj,x,y):
    #used to draw any object sent to it on the screen
    gameDisplay.blit(obj.image, (obj.x + x,obj.y + y))

def collide(plyr,obj,mapx,mapy):

    if obj.can_collide == False :
        return False
    elif ( ((plyr.x + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    elif ( ((plyr.x + plyr.w + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.w + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    elif ( ((plyr.x + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.h + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.h + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    elif ( ((plyr.x + plyr.w + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.w + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.h + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.h + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    else:
        return False

def load_map(name):
    path = 'maps/' + name + '.txt'
    f = open(path,'r')

    for l in f:
        a = l.split()

        if int(a[0]) == 0:
            #id of first line
            player1.x = float(a[1])
            player1.y = float(a[2])
            map1.map_edge_x = int(a[3])
            map1.map_edge_y = int(a[4])

        if int(a[0]) == 1:
            #id of wall
            wx = float(a[1])
            wy = float(a[2])
            wl = wall(wx,wy)
            objects.append(wl)

        if int(a[0]) == 2:
            #id of line
            lx1 = float(a[1])
            ly1 = float(a[2])
            lx2 = float(a[3])
            ly2 = float(a[4])
            ln = line(lx1,ly1,lx2,ly2)

            if lx2 != lx1:
                lm = (ly2-ly1)/(lx2-lx1)
            else:
                ln.is_vertical = True
            
            ln.slope = lm
            ln.length = ((lx2-lx1)**2 + (ly2-ly1)**2 )**0.5
            lines.append(ln)

        if int(a[0]) == 3:
            #id of door
            dx = float(a[1])
            dy = float(a[2])
            dr = door(wx,wy)
            objects.append(dr)
  
def draw_map(x,y):
    for obj in objects:
        draw(obj,x,y)
    draw(player1,0,0)



def isBetween(a, b, c):
    #copied from
    # http://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment#
    crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)
    if abs(crossproduct) > 0.00001 : return False   # (or != 0 if using integers) ........ sys.float_info.epsilon

    dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
    if dotproduct < 0 : return False

    squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
    if dotproduct > squaredlengthba: return False

    return True





#--------------------------------level editor loop -------------------------------------------------
def editloop():

    objs = []
    wall1 = wall(0,0)
    line1 = line(0,0,0,0)
    plyrx = -100
    plyry = -100
    gridmode = False
    selected_object = 'none'
    linepoint1 = False
    mousepress = False
    quit = False
    while quit == False:

        #events---------------------------------------------------------------------------------------------------
        for event in pygame.event.get():
        
            # event - quit
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                #close game if backspace is pressed
                #(made this shortcut as game cannot be closed in full screen)
                if event.key == pygame.K_BACKSPACE:
                    quit = True
                #toggles fulscreen mode when pressing esc
                if event.key == pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()

                if event.key == pygame.K_g:
                    if gridmode == False:
                        gridmode = True
                    else:
                        gridmode = False


                if event.key == pygame.K_w:
                    selected_object = 'wall'
                if event.key == pygame.K_l:
                    selected_object = 'line'
                if event.key == pygame.K_p:
                    selected_object = 'player'
                if event.key == pygame.K_SPACE:
                    selected_object = 'eraser'



                if event.key == pygame.K_s:
                    l1 = '0 ' + str(plyrx) + ' ' + str(plyry) +' 2200 2200\n'
                    f = open('maps/level1.txt','w+')
                    f.seek(0,0)
                    f.write(l1)

                    for o in objs:
                        if o.name == 'wall':
                            l = str(o.id) + ' ' + str(o.x) + ' ' + str(o.y) + '\n'
                        elif o.name == 'line':
                            l = str(o.id) + ' ' + str(o.x1) + ' ' + str(o.y1) + ' ' + str(o.x2) + ' ' + str(o.y2) + '\n'
                        f.write(l)

                    f.close()

                    
            if event.type == pygame.MOUSEBUTTONUP:
                mousepress = True
    
        gameDisplay.fill(white)

        for o in objs:
            if o.name == 'wall':
                gameDisplay.blit(o.image,(o.x,o.y))
            elif o.name == 'line':
                pygame.draw.line(gameDisplay,blue,(o.x1,o.y1),(o.x2,o.y2),1)

        mcoords = pygame.mouse.get_pos()
        
        if selected_object == 'wall':

            if gridmode == False:
                wall1.x = mcoords[0] - (wall1.w/2)
                wall1.y = mcoords[1] - (wall1.h/2)
            elif gridmode == True:
                mx = mcoords[0]
                while mx % 30 != 0:
                    mx -= 1
                my = mcoords[1]
                while my % 30 != 0:
                    my -= 1
                wall1.x = mx
                wall1.y = my

            if mousepress == True:
                wl = wall(wall1.x,wall1.y)
                objs.append(wl)
                

            gameDisplay.blit(wall1.image,(wall1.x,wall1.y))
            

        if selected_object == 'line':
            if linepoint1 == False:
                if gridmode == False:
                    line1.x1 = mcoords[0]
                    line1.y1 = mcoords[1]
                elif gridmode == True:
                    mx = mcoords[0]
                    while mx % 30 != 0:
                        mx -= 1
                    my = mcoords[1]
                    while my % 30 != 0:
                        my -= 1
                    line1.x1 = mx
                    line1.y1 = my   
                if mousepress == True:
                    linepoint1 = True


                pygame.draw.circle(gameDisplay,red,(line1.x1,line1.y1),3,0)

            else:
                if gridmode == False:
                    line1.x2 = mcoords[0]
                    line1.y2 = mcoords[1]
                elif gridmode == True:
                    mx = mcoords[0]
                    while mx % 30 != 0:
                        mx -= 1
                    my = mcoords[1]
                    while my % 30 != 0:
                        my -= 1
                    line1.x2 = mx
                    line1.y2 = my

                pygame.draw.circle(gameDisplay,red,(line1.x1,line1.y1),3,0)
                pygame.draw.circle(gameDisplay,red,(line1.x2,line1.y2),3,0)
                pygame.draw.line(gameDisplay,blue,(line1.x1,line1.y1),(line1.x2,line1.y2),1)   
                
                if mousepress == True:
                    linepoint1 = False
                    ln = line(line1.x1,line1.y1,line1.x2,line1.y2)
                    objs.append(ln)

        if selected_object == 'player':
            pygame.draw.circle(gameDisplay,red,mcoords,3,0)
            if mousepress == True:
                plyrx = mcoords[0]
                plyry = mcoords[1]

        mousepress = False
        
        if gridmode == True:
            for x in range(0,1300,30):
                pygame.draw.line(gameDisplay,black,(x,0),(x,1000),1)
            for y in range(0,700,30):
                pygame.draw.line(gameDisplay,black,(0,y),(1390,y),1)        

        pygame.draw.circle(gameDisplay,red,(plyrx,plyry),3,0)

        
        pygame.display.update()
        clock.tick(fps)










        
# main code
gameintro()
if mode == 'play':
    gameinit()
    gameloop()
elif mode == 'edit':
    editloop()
gameexit()


