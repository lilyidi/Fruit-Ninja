from pygame import *
from random import*
from math import *
import os
screen=display.set_mode((800,600))
running=True
circle=image.load("circle.png")
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
    screen.blit(circle,(395,295))
    if circle.get_rect(topleft=(395,295)):
        transform.scale2x(circle)
        screen.blit(circle,(300,400))
    display.flip()
            
quit()
