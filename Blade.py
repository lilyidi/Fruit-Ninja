#Blade
from random import*
from pygame import *
from math import *

blade=image.load("BladePoint.png")
screen=display.set_mode((800,600))
running=True
pos=[]
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    screen.fill((0,255,0))
    silver=(111,111,111)
    mouse.set_visible(True)
    mxn,myn=mx,my
    if mb[0]==1:
        mouse.set_visible(False)
        if pos==[]:
            pos.append((mx,my))
        pos.append((mx,my))
        if len(pos) > 1:
            draw.lines(screen,silver,False,pos,10)
        if len(pos)>10:
            del(pos[0])
        screen.blit(blade,(mx,my))
    else:
        pos=[]
    display.flip()
    time.wait(15)
quit()
