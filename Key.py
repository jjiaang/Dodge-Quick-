import pygame

class Key():

    def __init__(self,xpos,ypos):
        self.pickedUp = False
        self.x = xpos
        self.y = ypos
        self.color = (255,123,100)
        self.sizex = 20
        self.sizey = 20

    def getColor(self):
        # Returns the color of the player
        return self.color

    def drawKey(self,window):
        pygame.draw.rect(window, self.getColor(),(self.x,int(self.y),self.sizex,self.sizey))