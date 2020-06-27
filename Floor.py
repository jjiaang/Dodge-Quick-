import pygame
import random

pygame.init()

class Floor():

    def __init__(self,xpos,ypos,width,length):
        self.x = xpos
        self.y = ypos
        self.width = width
        self.length = length
        self.base = 580
        self.floorTurn = False
        self.velocity = 3.5
        self.direction = 1

        self.floorHeights = [486.5,423.25,463.25,324.25,455.25]

        self.floorPixelHeight = self.floorHeights[self.y]

    # Draws a floor
    def drawFloor(self,window):
        pygame.draw.rect(window, (200,120,0),(self.x,self.floorPixelHeight,self.length,self.width))