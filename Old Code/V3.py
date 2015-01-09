from pygame import *
from random import*
from math import *
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,10'

screen=display.set_mode((800,600))

myClock=time.Clock()
#images
waterPic=image.load("pics/watermelon.png").convert_alpha()
cocoPic=image.load("pics/Normals/Coconut.png").convert_alpha()
agreenPic=image.load("pics/Normals/Apple Green.png").convert_alpha()
aredPic=image.load("pics/Normals/Apple Red.png").convert_alpha()
lemonPic=image.load("pics/Normals/Lemon.png").convert_alpha()
mangoPic=image.load("pics/Normals/Mango.png").convert_alpha()
orangePic=image.load("pics/Normals/Orange.png").convert_alpha()
pearPic=image.load("pics/Normals/Pear.png").convert_alpha()
pinePic=image.load("pics/Normals/Pineapple.png").convert_alpha()
tomatoPic=image.load("pics/Normals/Tomato.png").convert_alpha()

#sliced fruitPics
waterSlice=image.load("pics/Sliced/water.png").convert_alpha()
cocoSlice=image.load("pics/Sliced/coco.png").convert_alpha()
##agreenSlice=image.load("pics/Sliced/

""" USE THIS: atan2 """
fruitPics=[waterPic,cocoPic,agreenPic,aredPic,lemonPic,mangoPic,orangePic,pearPic,
        pinePic,tomatoPic]
fruits=[]
pts=[]

throwType=[1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,8,8,9,9,10]
pos=[]
running=True
def randomFruit():
    fruit=[choice(fruitPics),randint(100,600),600,randint(-5,5),-15]
    return fruit
def moveFruit(fruit):
##    fruit=randomFruit()
    fruit[X]+=fruit[VX]
    fruit[Y]+=fruit[VY]
    fruit[VY]+=.2
##def moreFruit():
##    for i in range(choice(throwType)):
##        fruits.append(choice(fruitPics))
##    for fruit in fruits:
##        randomFruit()[0]=fruit
##        moveFruit(randomFruit)
def sliceFruit(fruit):
    pos=[]
    nmy,nmy=my,my
#    if atn2(my-nmy,mx-nmy)
counter=0
click=False
PIC=0
X=1
Y=2
VX=3
VY=4
collide=False
fruit=randomFruit()
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        back=screen.copy()
        if evt.type==MOUSEBUTTONDOWN:
            click=True
        if evt.type==MOUSEBUTTONUP:
            click=False
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    moveFruit(fruit)
##    moreFruit()
    screen.fill((0,0,0))
    screen.blit(fruit[PIC],(fruit[X],fruit[Y]))
    if mb[0]==1:
        pts.append((mx,my))
    if click and fruit[PIC].get_rect(topleft=(fruit[X],fruit[Y])).collidepoint(mx,my):
        click = False
        print "slice"
    myClock.tick(60)
    display.flip()
    if fruit[Y]>650 or fruit[X]<-100 or fruit[X]>1000:
        fruit = randomFruit() #credit to simon
##        sliceFruit(fruit)
##    if mb[0]==1 and fruit[PIC].get_rect(topleft=(fruit[X],fruit[Y])).collidepoint(mx,my): #credit to simon
##        collide=True
##    if collide==True:
##        screen.blit(waterSlice,(fruit[X],fruit[Y]))
##        print "slice"
##        collide=False
quit()
