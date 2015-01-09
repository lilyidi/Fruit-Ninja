from pygame import *
from random import*
from math import *
import os
screen=display.set_mode((800,600))
#images
waterPic=image.load("pics/watermelon.png").convert_alpha() #<---credit to simon 
cocoPic=image.load("pics/Normals/Coconut.png").convert_alpha()
agreenPic=image.load("pics/Normals/Apple Green.png").convert_alpha()
aredPic=image.load("pics/Normals/Apple Red.png").convert_alpha()
lemonPic=image.load("pics/Normals/Lemon.png").convert_alpha()
mangoPic=image.load("pics/Normals/Mango.png").convert_alpha()
orangePic=image.load("pics/Normals/Orange.png").convert_alpha()
pearPic=image.load("pics/Normals/Pear.png").convert_alpha()
pinePic=image.load("pics/Normals/Pineapple.png").convert_alpha()
tomatoPic=image.load("pics/Normals/Tomato.png").convert_alpha()
strawPic=image.load("pics/Normals/Strawberry.png").convert_alpha()

###bombs
##arcBomb=image.load("pics/Arcade Bomb.png").convert_alpha()
##classBomb=image.load("pics/Classic Bomb.png").convert_alpha()
##spiritBomb=image.load("pics/Spirit Bomb.png").convert_alpha()

#sliced fruitPics
waterSlice=image.load("pics/Sliced/water.png").convert_alpha()
cocoSlice=image.load("pics/Sliced/coco.png").convert_alpha()
agreenSlice=image.load("pics/Sliced/agreen.png").convert_alpha()
aredSlice=image.load("pics/Sliced/apple.png").convert_alpha()
lemonSlice=image.load("pics/Sliced/lemon.png").convert_alpha()
mangoSlice=image.load("pics/Sliced/Mango.png").convert_alpha()
orangeSlice=image.load("pics/Sliced/orange.png").convert_alpha()
pearSlice=image.load("pics/Sliced/pear.png").convert_alpha()
pineSlice=image.load("pics/Sliced/pineapple1.png").convert_alpha()
tomatoSlice=image.load("pics/Sliced/tomato.png").convert_alpha()
strawSlice=image.load("pics/Sliced/straw.png").convert_alpha()
waterSlice2=image.load("pics/Sliced/water2.png").convert_alpha()
cocoSlice2=image.load("pics/Sliced/coco2.png").convert_alpha()
agreenSlice2=image.load("pics/Sliced/agreen2.png").convert_alpha()
aredSlice2=image.load("pics/Sliced/apple2.png").convert_alpha()
lemonSlice2=image.load("pics/Sliced/lemon2.png").convert_alpha()
mangoSlice2=image.load("pics/Sliced/mango2.png").convert_alpha()
orangeSlice2=image.load("pics/Sliced/orange2.png").convert_alpha()
pearSlice2=image.load("pics/Sliced/pear2.png").convert_alpha()
pineSlice2=image.load("pics/Sliced/pineapple2.png").convert_alpha()
tomatoSlice2=image.load("pics/Sliced/tomato2.png").convert_alpha()
strawSlice2=image.load("pics/Sliced/straw2.png").convert_alpha()

#blade
blade=image.load("BladePoint.png")


""" USE THIS: atan2 """
fruitPics=[waterPic,cocoPic,agreenPic,aredPic,mangoPic,orangePic,pearPic, pinePic,tomatoPic,lemonPic,strawPic]
fruitSlices=[waterSlice,cocoSlice,agreenSlice,aredSlice,mangoSlice,orangeSlice,pearSlice,pineSlice,tomatoSlice,lemonSlice,strawSlice]
fruitSlices2=[waterSlice2,cocoSlice2,agreenSlice2,aredSlice2,mangoSlice2,orangeSlice2,pearSlice2,pineSlice2,tomatoSlice2,lemonSlice2,strawSlice2]
fruits=[]
slicedFruits=[]
slicedFruits2=[]
"""
[type,x,y,vx,vy]
"""

throwType=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,5]

def randomFruit():
    '''places a random fruit at a random spot'''
    power = randint(-2,2)
    x=randint(100,600)
    if x>300:
        vx=randint(-2,0)
    else:
        vx=randint(0,2)
    fruit=[choice(fruitPics),x,600,vx+power,-15+power,20]
    return fruit

def getRect(fruit):
    '''gets the rect of the image of the fruit'''
    return fruit[PIC].get_rect(topleft=(fruit[X],fruit[Y])) #credit to Simon Tang

def moveFruit(fruits):
    '''moves the fruits on the screen'''
    for fru in fruits:
        fruits[fruits.index(fru)][X]+=fru[VX]
        fruits[fruits.index(fru)][Y]+=fru[VY]
        fruits[fruits.index(fru)][VY]+=.25

##def moveFFruits(fruits):
##    for fruit in fruits:
##        fruit[fruits.index{fruit)][X]=choice([0,800])+=
##        fruit[

def moveSFruit(sfruit):
    '''moves the sliced fruits on the screen'''
    sfruit[X]-=sfruit[VX]
    sfruit[Y]+=sfruit[VY]
    sfruit[VY]+=1
    sfruit[VX]+=.1
    
def moveSFruit2(sfruit):
    sfruit[X]+=sfruit[VX]
    sfruit[Y]+=sfruit[VY]
    sfruit[VY]+=1
    sfruit[VX]+=.1
    
#credit to Sean /////////////////////////      
def sliceFruit(fruits,omx,omy):
    global points
    mx,my=mouse.get_pos()
    dist=((omx-mx)**2+(omy-my)**2)**.5
    if dist==0:
        dist=1
        for fruit in fruits:
            if getRect(fruit).collidepoint(mx,my):
                del(fruits[fruits.index(fruit)])
                points += 1
                slicedFruits.append([fruitSlices[fruitPics.index(fruit[PIC])],mx-30,my,fruit[VX],fruit[VY]])
                slicedFruits2.append([fruitSlices2[fruitPics.index(fruit[PIC])],mx+30,my,fruit[VX],fruit[VY]])
    else:
        sx=(mx-omx)/dist
        sy=(my-omy)/dist
        for i in range(int(dist)):
            for fruit in fruits:
                if getRect(fruit).collidepoint(int(omx+i*sx),int(omy+i*sy)):
                    del (fruits[fruits.index(fruit)])
                    points += 1
#////////////////////////////////////
##                    sfruit=[fruit[0],mx,my,randint(-5,5),randint(-5,5)]
                    slicedFruits.append([fruitSlices[fruitPics.index(fruit[PIC])],mx-30,my,fruit[VX],fruit[VY]])
                    slicedFruits2.append([fruitSlices2[fruitPics.index(fruit[PIC])],mx+30,my,fruit[VX],fruit[VY]])
    return mx,my
mx,my,omx,omy=0,0,0,0
pts=[]
angs=[]
def subtract(a,b):
    return a-b
def combo():
    global mx,my,omx,omy
    mx,my=mouse.get_pos()
    if getRect(fruit).collidepoint(mx,my):
        mx,my=mouse.get_pos()
        pts.append([mx,my])
        if len(pts)>1:
            for i in range(len(pts)-2):
                if (pts[i][0]-pts[i+1][0])==0:
                    slope="unde"
                else:
                    slope=(pts[i][1]-pts[i+1][1])/(pts[i][0]-pts[i+1][0])  
##                angs.append(atan2(pts[i][0]-pts[i+1][0],pts[i][1]-pts[i+1][1]))
    print pts
#Set-up
display.set_caption("Ninja of them Fruits")
font.init()
comicFont = font.SysFont("Comic Sans MS", 70)
os.environ['SDL_VIDEO_WINDOW_POS'] = '30,50'
myClock=time.Clock()
running=True

points=0
click=False
PIC=0
X=1
Y=2
VX=3
VY=4
ANG=5
collide=False
fruit=randomFruit()

points = 0

silver=(111,111,111)

#Running loop
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        back=screen.copy()
        if evt.type==MOUSEBUTTONDOWN:
            click=True
            mx,my=mouse.get_pos()
        if evt.type==MOUSEBUTTONUP:
            click=False
            
#Limiting how many fruits are on the screen
#credit to sean    
    if len(fruits) > 0:
        if randint(1,40*len(fruits)) == 5:
            for i in range(choice(throwType)):
                fruits.append(randomFruit())
    else:
        for i in range(choice(throwType)):
            fruits.append(randomFruit())
#/////////////////////
    
    
    moveFruit(fruits)
    
    screen.fill((0,0,0))
    for each in fruits:
        screen.blit(each[0],(each[X],each[Y]))
##        each[PIC]=transform.rotate(each[PIC],each[ANG])

    for each in fruits:
        if each[Y]>650 or each[X]<-100 or each[X]>1000:
            del (fruits[fruits.index(each)])
    if click:
        mx,my = sliceFruit(fruits,mx,my)
        combo()
    for fruit in slicedFruits:
        moveSFruit(fruit)
        screen.blit(fruit[PIC],(fruit[X],fruit[Y]))
        if fruit[Y]>620:
            del (slicedFruits[slicedFruits.index(fruit)])
    for fruit in slicedFruits2:
        moveSFruit2(fruit)
        screen.blit(fruit[PIC],(fruit[X],fruit[Y]))
        if fruit[Y]>620:
            del (slicedFruits2[slicedFruits2.index(fruit)])
        
    #some animation awesomeness
#blade        
    mb=mouse.get_pressed()
    mouse.set_visible(True)
    
    if mb[0]==1:
        mxn,myn=mx,my
        mouse.set_visible(False)
        if pos==[]:
            pos.append((mx,my))
        pos.append((mx,my))
        if len(pos) > 1:
            draw.lines(screen,silver,False,pos,10)
        if len(pos)>7:
            del(pos[0])
        screen.blit(blade,(mx,my))
    else:
        pos=[]
#/////////////////////

    pic = comicFont.render(str(points),True,(255,255,255))
    screen.blit(pic,(0,0))
    myClock.tick(60)
    display.flip()
            
quit()
