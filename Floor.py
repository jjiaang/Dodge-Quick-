import pygame

pygame.init()

class Floor():

    def __init__(self,xpos,ypos,width,length):
        self.x = xpos
        self.y = ypos
        self.width = width
        self.length = length

    # Draws a floor
    def drawFloor(self,window):
        pygame.draw.rect(window, (255,0,0),(self.x,self.y,self.length,self.width))