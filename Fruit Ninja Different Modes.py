from pygame import *
from random import*
from math import *
import os
import datetime
screen=display.set_mode((800,600))
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
strawPic=image.load("pics/Normals/Strawberry.png").convert_alpha()

#Specials
dragonPic=image.load("pics/Specials/Dragonfruit.png").convert_alpha()
pomePic=image.load("pics/Specials/Pomegranate.png").convert_alpha()
freezeBanaPic=image.load("pics/Specials/Freeze Banana.png").convert_alpha()
frenzyBanaPic=image.load("pics/Specials/Frenzy Banana.png").convert_alpha()
pointsBanaPic=image.load("pics/Specials/Points Banana.png").convert_alpha()
spiritBanaPic=image.load("pics/Specials/Spirit Banana.png").convert_alpha()
arcBombPic=image.load("pics/Specials/Arcade Bomb.png").convert_alpha()
spiritBombPic=image.load("pics/Specials/Spirit Bomb.png").convert_alpha()

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

#Special Slices
freezeSlice=image.load("pics/Sliced/freeze1.png").convert_alpha()
freezeSlice2=image.load("pics/Sliced/freeze2.png").convert_alpha()
frenzySlice=image.load("pics/Sliced/frenzy1.png").convert_alpha()
frenzySlice2=image.load("pics/Sliced/frenzy2.png").convert_alpha()
pointsSlice=image.load("pics/Sliced/points.png").convert_alpha()
pointsSlice2=image.load("pics/Sliced/points2.png").convert_alpha()
dragonSlice=image.load("pics/Sliced/dragon.png").convert_alpha()
dragonSlice2=image.load("pics/Sliced/dragon2.png").convert_alpha()


#blade
blade=image.load("BladePoint.png")

#END
end=image.load("Pics/Cutscenes/Ending.png")
end=transform.smoothscale(end,screen.get_size())

#TO MAKE LIFE EASIER
'''lists of images'''
fruitPics=[waterPic,cocoPic,agreenPic,aredPic,mangoPic,orangePic,pearPic, pinePic,tomatoPic,lemonPic,strawPic]#<-----add pomegranate later, strawberry
banaPics=[frenzyBanaPic,pointsBanaPic]  #Add spirit
banaSlices=[frenzySlice,pointsSlice]
banaSlices2=[frenzySlice2,pointsSlice2]
bombs=[arcBombPic]
fruitSlices=[waterSlice,cocoSlice,agreenSlice,aredSlice,mangoSlice,orangeSlice,pearSlice,pineSlice,tomatoSlice,lemonSlice,strawSlice]
fruitSlices2=[waterSlice2,cocoSlice2,agreenSlice2,aredSlice2,mangoSlice2,orangeSlice2,pearSlice2,pineSlice2,tomatoSlice2,lemonSlice2,strawSlice2]

fruits=[]
slicedFruits=[]
slicedFruits2=[]

throwType=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,5]
level=0

def randomFruit():
    '''places a random fruit at a random spot (bombs are considered fruits)'''
    power = randint(-2,2)
    x=randint(100,600)
    dragonProb=randint(1,100)
    bombProb=randint(1,20)
    bananaProb=randint(1,50)
    if x>300:
        vx=randint(-2,0)
    else:
        vx=randint(0,2)
    if dragonProb==1:
        fruitPic=dragonPic
    elif bombProb==1:
        fruitPic=choice(bombs)  #<------------------change later
    elif bananaProb==1:
        fruitPic=choice(banaPics)
    else:
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

def movefFruits(fruits):
    '''moves the frenzy fruits'''
    for fruit in fruits:
        fruit[X]=choice([0,800])
        fruit[Y]=200
        fruit[VY]=randint(-5,-2)
        if fruit[X]==0:
            fruit[VX]=5+randint(-2,7)
        else:
            fruit[VX]=-5+randint(-7,2)
        fruit[X]+=fruit[VX]
        fruit[Y]+=fruit[VY]
        fruit[VY]+=.25
        
def frenzy():
    '''when the frenzy banana is sliced'''
    global fruits
    fruits=[]
    throwType=[5,5,5,6,6,6,6,7,7,7,8,8,9,10]
    now=time.get_ticks()
    end=now+5000
    for i in range(7):
        for i in range(choice(throwType)):
            fruit=randomFruit()
            if fruit[PIC]!=arcBombPic and fruit[PIC] not in banaPics:
                fruits.append(fruit)
        movefFruits(fruits)
        for fruit in fruits:
            screen.blit(fruit[PIC],(fruit[X],fruit[Y]))
def slowMoveFruits(fruits):
    '''moves the fruits while the freeze banana is activated'''
    for fruit in fruits:
        fruit[X]+=fruit[VX]
        fruit[Y]+=fruit[VY]
        fruit[VY]+=.01
        fruit[VX]+=.01
def freeze():
    '''when freeze banana is activated'''
    global normal
    global fruits
    global limit
    freezeTime=time.get_ticks()+5000
    slowMoveFruits(fruits)
    for fruit in fruits:
        screen.blit(fruit[PIC],(fruit[X],fruit[Y]))
    for fruit in fruits:
        screen.blit(fruit[PIC],(fruit[X],fruit[Y]))
    normal=True
    timeMark=False
##    return timesec,normal

def pointsBanana():
    '''when points banana is activated'''
    global fruits
    pointsTime=5000
##    if pointsTime>0:
##        for fruit in fruits:
##            if fruit[PIC]!=arcBombPic:
##                if getRect(fruit).collidepoint(mx,my):
##                    banapoints+=
##    print banapoints
##    pointsMark=False
    return pointsTime

def moveSFruit(sfruit):
    '''moves the sliced fruits on the screen'''
    sfruit[X]-=sfruit[VX]
    sfruit[Y]+=sfruit[VY]
    sfruit[VY]+=1
    sfruit[VX]+=.1
    
def moveSFruit2(sfruit):
    '''moves the other half of the sliced fruits on the screen'''
    sfruit[X]+=sfruit[VX]
    sfruit[Y]+=sfruit[VY]
    sfruit[VY]+=1
    sfruit[VX]+=.1

def sliceBana(bana):
    slicedFruits.append([banaSlices[banaPics.index(bana[PIC])], mx-30,my,bana[VX],bana[VY]])
    slicedFruits2.append([banaSlices2[banaPics.index(bana[PIC])], mx+30,my,bana[VX],bana[VY]])

def sliceDragon(dragon):
    slicedFruits.append([dragonSlice,mx-30,my,dragon[VX],dragon[VY]])
    slicedFruits2.append([dragonSlice2,mx-30,my,dragon[VX],dragon[VY]])
     
def sliceFruit(fruits,omx,omy):
    '''slices the fruits'''
    global points
    mx,my=mouse.get_pos()
    dist=((omx-mx)**2+(omy-my)**2)**.5
    if dist==0:
        dist=1
        for fruit in fruits:
            if getRect(fruit).collidepoint(mx,my):
                if fruit[PIC]==arcBombPic:
                    del(fruits[fruits.index(fruit)])
                    if points>=10:
                        points-=10
                    else:
                        points=0
                    fruits=[]
                elif fruit[PIC] in banaPics:
                    sliceBana(fruit)
                    points+=5
                    if fruit[PIC]==frenzyBanaPic:
                        normal=False
                        frenzy()
                    elif fruit[PIC]==freezeBanaPic:
                        freezeMark=True
                        normal=False
                        freeze()
                    else:
                        pointsMark=True
                    del(fruits[fruits.index(fruit)])
                elif fruit[PIC]==dragonPic:
                    sliceDragon(fruit)
                    points+=50
                    del(fruits[fruits.index(fruit)])
                else:
                    points+= 1
                    slicedFruits.append([fruitSlices[fruitPics.index(fruit[PIC])],mx-30,my,fruit[VX],fruit[VY]])
                    slicedFruits2.append([fruitSlices2[fruitPics.index(fruit[PIC])],mx+30,my,fruit[VX],fruit[VY]])
                    del(fruits[fruits.index(fruit)])
    else:
        sx=(mx-omx)/dist
        sy=(my-omy)/dist
        for i in range(int(dist)):
            for fruit in fruits:
                if getRect(fruit).collidepoint(int(omx+i*sx),int(omy+i*sy)):
                    if fruit[PIC]==arcBombPic:
                        del(fruits[fruits.index(fruit)])
                        if points>=10:
                            points-=10
                        else:
                            points=0
                        fruits=[]
                    elif fruit[PIC] in banaPics:
                        points+=5
                        sliceBana(fruit)
                        if fruit[PIC]==frenzyBanaPic:
                            frenzy()
                        elif fruit[PIC]==freezeBanaPic:
                            freezeMark=True
                            normal=False
                            freeze()
                        else:
                            pointsMark=True
                            myClock.tick()
                            if pointsTime>0:
                                for fruit in fruits:
                                    if fruit[PIC]!=arcBombPic:
                                        if getRect(fruit).collidepoint(mx,my):
                                            points+=2
                                            print (points)
                            else:
                                points+=1
                            del(fruits[fruits.index(fruit)])
                    elif fruit[PIC]==dragonPic:
                        points+=50
                        sliceDragon(fruit)
                        del(fruits[fruits.index(fruit)])
                    else:
                        points += 1
                        slicedFruits.append([fruitSlices[fruitPics.index(fruit[PIC])],mx-30,my,fruit[VX],fruit[VY]])
                        slicedFruits2.append([fruitSlices2[fruitPics.index(fruit[PIC])],mx+30,my,fruit[VX],fruit[VY]])
                        del(fruits[fruits.index(fruit)])
    return mx,my #to move sliced fruits later
#MENU STUFF
def menu():
    running = True
    myClock = time.Clock()
    buttons=[Rect(229,84,351,110),Rect(225,250,351,110),Rect(226,429,110,351)]
    vals=["Classic","Arcade","Start"]
    instructions=image.load("Pics/Menu/Instructions menu.png").convert_alpha()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        screen.fill((111,150,111))
        screen.blit(instructions,(0,0))
        for r,v in zip(buttons,vals):
            if r.collidepoint(mpos):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    return v
            else:
                draw.rect(screen,(255,255,0),r,2)
                
        display.flip()

def Arcade():
    running = True
    inst = image.load("Pics/Menu/Arcade.png")
    inst2=image.load("Pics/Menu/Arcade2.png")
    inst = transform.smoothscale(inst, screen.get_size())
    inst2=transform.smoothscale(inst2, screen.get_size())
    screen.blit(inst,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        nextButton=Rect(570,490,250,115)
        if mb[0]==1 and nextButton.collidepoint(mx,my):
            screen.blit(inst2,(0,0))
        display.flip()
    return "start"

def Start():
    running=True
    cutscenes=[]
    click=False
    for i in range(10):
        pic=image.load("Pics/Cutscenes/Cutscene "+str(i)+".png").convert_alpha()
        cutscenes.append(transform.smoothscale(pic,screen.get_size()))
    num=0
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT or (click and num>9):
                running = False
            if evnt.type==MOUSEBUTTONDOWN:
                click=True
        if click and num<=9:
            screen.blit(cutscenes[num],(0,0))
            num+=1
            click = False
        display.flip()
    return "game"

running=True
#Set-up
display.set_caption("Ninja of them Fruits")
font.init()
comicFont = font.SysFont("Comic Sans MS", 50)
timeFont=font.SysFont("Comic Sans MS",40)
os.environ['SDL_VIDEO_WINDOW_POS'] = '30,50'
myClock=time.Clock()
running=True


click=False
normal=True
PIC=0
X=1
Y=2
VX=3
VY=4
ANG=5

points = 0

silver=(111,111,111)
level=1
limit=60
page="menu"
freezeMark=False
while page!="game":
    if page=="menu":
        page=menu()
    if page=="Start":
        page=Start()
##    if page=="Arcade":
##        page=Arcade()
if page=="game":
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
        if len(fruits) > 0:
            if randint(1,40*len(fruits)) == 5:
                for i in range(choice(throwType)):
                    fruit=randomFruit()
                    if fruit[PIC]!=arcBombPic:
                        fruits.append(randomFruit())
                                    
        else:
            for i in range(choice(throwType)):
                fruits.append(randomFruit())
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        if normal==True:
            moveFruit(fruits)
        screen.fill((0,0,0))
        for each in fruits:
            screen.blit(each[0],(each[X],each[Y]))

        for each in fruits:
            if each[Y]>650 or each[X]<-100 or each[X]>1000:
                del (fruits[fruits.index(each)])
        if click:
            mx,my = sliceFruit(fruits,mx,my)
##            if pointsMark:
##                if myClock.get_time()
##                points+=1
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
        sec=time.get_ticks()//1000
        if sec<=60:
            if sec<10:
                timesec="0"+str(sec)
            elif sec==60:
                timesec=00
            else:
                timesec=sec
            timeleft=str(sec//60)+":"+str(timesec)
        else:
            page="end"
            screen.blit(end,(0,0))
            pointspic=timeFont.render("You scored: "+str(points),True,(255,0,0))
            screen.blit(pointspic,(400,300))
            display.flip()
            time.wait(6000)
            break
        timepic=timeFont.render(timeleft,True,(255,255,255))
        pic = comicFont.render(str(points),True,(255,255,255))
        screen.blit(timepic,(715,0))
        screen.blit(pic,(0,0))
        myClock.tick(60)
        display.flip()
quit()
