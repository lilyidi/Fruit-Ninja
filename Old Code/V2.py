from pygame import *
from random import*
from math import *
import os
import datetime
screen=display.set_mode((800,600))

#Set-up
display.set_caption("Fruit Apprentice!")
font.init()
comicFont = font.SysFont("Comic Sans MS", 50)
timeFont=font.SysFont("Comic Sans MS",40)
os.environ['SDL_VIDEO_WINDOW_POS'] = '30,50'
myClock=time.Clock()
running=True

#images
waterPic=image.load("pics/Normals/watermelon.png").convert_alpha() #<---credit to simon 
cocoPic=image.load("pics/Normals/Coconut.png").convert_alpha()
agreenPic=image.load("pics/Normals/Apple Green.png").convert_alpha()
aredPic=image.load("pics/Normals/Apple Red.png").convert_alpha()
lemonPic=image.load("pics/Normals/Lemon.png").convert_alpha()
mangoPic=image.load("pics/Normals/Mango.png").convert_alpha()
orangePic=image.load("pics/Normals/Orange.png").convert_alpha()
pearPic=image.load("pics/Normals/Pear.png").convert_alpha()
pinePic=image.load("pics/Normals/Pineapple.png").convert_alpha()
tomatoPic=image.load("pics/Normals/Tomato.png").convert_alpha()

#Specials
strawPic=image.load("pics/Specials/Strawberry.png").convert_alpha()
dragonPic=image.load("pics/Specials/Dragonfruit.png").convert_alpha()
pomePic=image.load("pics/Specials/Pomegranate.png").convert_alpha()
freezeBanaPic=image.load("pics/Specials/Freeze Banana.png").convert_alpha()
frenzyBanaPic=image.load("pics/Specials/Frenzy Banana.png").convert_alpha()
pointsBanaPic=image.load("pics/Specials/Points Banana.png").convert_alpha()
spiritBanaPic=image.load("pics/Specials/Spirit Banana.png").convert_alpha()
arcBombPic=image.load("pics/Specials/Arcade Bomb.png").convert_alpha()
classBombPic=image.load("pics/Specials/Classic Bomb.png").convert_alpha()
#spiritBomb=image.load("pics/Specials/Spirit Bomb.png").convert_alpha()

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

#cutscenes
cut0=image.load("PICS/Cutscenes/Cutscene 0.png")
cut1=image.load("PICS/Cutscenes/Cutscene 1.png")
cut2=image.load("PICS/Cutscenes/Cutscene 2.png")
cut3=image.load("PICS/Cutscenes/Cutscene 3.png")
cut4=image.load("PICS/Cutscenes/Cutscene 4.png")
cut5=image.load("PICS/Cutscenes/Cutscene 5.png")
cut6=image.load("PICS/Cutscenes/Cutscene 6.png")
cut7=image.load("PICS/Cutscenes/Cutscene 7.png")
cut8=image.load("PICS/Cutscenes/Cutscene 8.png")
cut9=image.load("PICS/Cutscenes/Cutscene 9.png")
cut10=image.load("PICS/Cutscenes/Cutscene 10.png")
cut11=image.load("PICS/Cutscenes/Cutscene 11.png")
cut13=image.load("PICS/Cutscenes/Cutscene 13.png")
cut14=image.load("PICS/Cutscenes/Cutscene 14.png")
cut15=image.load("PICS/Cutscenes/Cutscene 15.png")
cut16=image.load("PICS/Cutscenes/Cutscene 16.png")
cut17=image.load("PICS/Cutscenes/Cutscene 17.png")
cut18=image.load("PICS/Cutscenes/Cutscene 18.png")
EndYAY=image.load("PICS/Cutscenes/Ending.png")

#Menuuuuus

startmenu=image.load("PICS/Menu/Start Screen.png")
mainmenu=image.load("PICS/Menu/Main Menu.png")
arc1menu=image.load("PICS/Menu/Arcade.png")
arc2menu=image.load("PICS/Menu/Arcade2.png")
arc3menu=image.load("PICS/Menu/Arcade3.png")

""" USE THIS: atan2 """
fruitPics=[waterPic,cocoPic,agreenPic,aredPic,mangoPic,orangePic,pearPic, pinePic,tomatoPic,lemonPic,strawPic]#<-----add pomegranate later
banaPics=[freezeBanaPic,frenzyBanaPic,pointsBanaPic,spiritBanaPic]
bombPics=[arcBombPic,classBombPic]
specPics=[dragonPic]
fruitSlices=[waterSlice,cocoSlice,agreenSlice,aredSlice,mangoSlice,orangeSlice,pearSlice,pineSlice,tomatoSlice,lemonSlice,strawSlice]
fruitSlices2=[waterSlice2,cocoSlice2,agreenSlice2,aredSlice2,mangoSlice2,orangeSlice2,pearSlice2,pineSlice2,tomatoSlice2,lemonSlice2,strawSlice2]
#slices for specs too ><
fruits=[]
slicedFruits=[]
slicedFruits2=[]

throwType=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,5]
level=0
ac="Arcade"

#Fitting to Screen
scenes=[startmenu,mainmenu,arc1menu,arc2menu,arc3menu,cut0,cut1,cut2,cut3,cut4,cut5,cut6,cut7,cut8,cut9,cut10,cut11,cut13,cut14,cut15,cut16,cut17,cut18,EndYAY]
for i in range(len(scenes)):
   scenes[i]=transform.smoothscale(scenes[i], screen.get_size())
    
#defining Menu and co.

def start():
    '''starting screen'''
    global flag1
    global running
    screen.blit(startmenu,(0,0))
    startbutton=Rect(195,380,392,110)
    mx,my=mouse.get_pos()
    if startbutton.collidepoint(mx,my):
        draw.rect(screen,(0,0,0),startbutton,5)
        if click:
            flag1=True
##            beginCutscene()
    #Credit to Angus
    if flag1:
        beginCutscene()
        running=False

def beginCutscene():
    '''storyline'''
    for i in range(0,15):
        screen.blit(scenes[i],(0,0))
        time.wait(600)
        display.flip()
    return True
            

#THE FLAGS
GAMESTART=False
click=False
flag1=False
GAMESTART=start()

#Starting the start menu
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        mx,my=mouse.get_pos()
        back=screen.copy()
        if evt.type==MOUSEBUTTONDOWN:
            click=True
        if evt.type==MOUSEBUTTONUP:
            click=False           
    start()
    display.flip()
GAMESTART=True
#LEVELS (NOT BEING USED)
def level1():
    if points>=200:
        return 2
    else:
        return 1
def level2():
    numfrenzy=0
    if fruit[PIC]==frenzyBanaPic and getRect(fruit).collidepoint(mx,my):
        numfrenzy+=1
    if numfrnezy>=3:
        return 3
    else:
        return 2
def level3():
    if fruit[PIC]==pointsBanaPic and getRect(fruit).collidepoint(mx,my):
        banapoints=0
        if get(fruit).collidepoint(mx,my) and fruit[PIC]!=arcBombPic:
            banapoints+=1
            if fruit[PIC]==dragonPic:
                banapoints+=50
        if banapoints>=100:
            return 4
    else:
        return 3
def level4():
    nosscore=0
    if getRect(fruit).collidepoint(mx,my):
        if fruit[PIC]!=strawPic and fruit[PIC]!=arcBombPic: 
            nosscore+=1
        if fruit[PIC]==dragonPic:
            nosscore+=50
        if fruit[PIC]==strawPic:
            nosscore=0
    if nosscore>=250:
        return 5
    else:
        return 4
def level5():
    if points>=300:
        return "FINAL"
    else:
        return 5
def levelFINAL():
    ppoints=pomegranate()
    if ppoints>=40:
        return "End"
    elif ppoint>=30:
        return 5
    elif ppoint>=20:
        return 4
    elif ppoint>=10:
        return 3
    else:
        return 2
def randomFruit():
    '''places a random fruit at a random spot'''
    power = randint(-2,2)
    x=randint(100,600)
##    dragonProb=randint(1,2)
##    bombProb=randint(1,2)
##    bananaProb=randint(1,20)
    if x>300:
        vx=randint(-2,0)
    else:
        vx=randint(0,2)
##    if dragonProb==1:
##        fruitPic=dragonPic
##    if bombProb==1:
##        fruitPic=choice(bombPics)  #<------------------change later
##    if bananaProb==1:
##        fruitPic=choice(banaPics)
##    else:
    fruitPic=choice(fruitPics)
    fruit=[fruitPic,x,600,vx+power,-15+power,20]
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

##def SpecFruit(specfruits):

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

#    if atan2(my-nmy,mx-nmy)
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
level=1
#Running loop
if GAMESTART==True:
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

    #TIME:
        sec=time.get_ticks()/1000
        if sec<=60:
            if sec<10:
                timesec="0"+str(sec)
            else:
                timesec=sec
            timeleft=str(sec/60)+":"+str(timesec)

        else:
            break #CHANGE
        timepic=timeFont.render(timeleft,True,(255,255,255))
        pic = comicFont.render(str(points),True,(255,255,255))
        screen.blit(timepic,(715,0))
        screen.blit(pic,(0,0))
        myClock.tick(60)
        display.flip()
                
    quit()
