import pygame

pygame.init()

class Floor():

    def __init__(self,xpos,ypos,width,length):
        self.x = xpos
        self.y = ypos
        self.width = width
        self.length = length
        self.base = 580

        self.floorHeights = [486.5,411.15]

        self.floorPixelHeight = self.floorHeights[self.y]

    # Draws a floor
    def drawFloor(self,window):
        pygame.draw.rect(window, (255,0,0),(self.x,self.floorPixelHeight,self.length,self.width))