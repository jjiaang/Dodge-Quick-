import pygame

pygame.init()

class Floor():

    def __init__(self,xpos,ypos,width,length):
        self.x = xpos
        self.y = ypos
        self.width = width
        self.length = length

        self.floorHeights = [441,442,442,442,443,444,445,446,449,451,454,458,462,467,472,479,486,494,503,513,524,536,549,564]

        self.floorPixelHeight = self.floorHeights[self.y]

    # Draws a floor
    def drawFloor(self,window):
        pygame.draw.rect(window, (255,0,0),(self.x,self.floorPixelHeight,self.length,self.width))