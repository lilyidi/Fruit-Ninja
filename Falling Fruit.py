from pygame import *
from random import*
screen=display.set_mode((1024,768))
#images
waterPic=image.load("pics/normals/watermelon.png")
waterRect=(260,768,62,100)
running=True
def flyingFruit(fruit,fruitRect):
    back=screen.copy()
    x=fruitRect[0]
    #y=768
    while y<=800:
        screen.blit(back,(0,0))
        screen.blit(fruit,fruitRect)
        fruitRect=(x,y,fruitRect[2],fruitRect[3])
        x+=1
        y=(x-300)**2/100+20
##        time.wait(5)
        display.flip()
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        back=screen.copy()
    flyingFruit(waterPic,waterRect)
    display.flip()
quit()
