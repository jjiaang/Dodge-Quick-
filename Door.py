import pygame

class Door():

    def __init__(self,xpos,ypos):
        self.entered = False
        self.x = xpos
        self.y = ypos
        self.color = (210,105,30)
        self.sizex = 40
        self.sizey = 80

    def drawDoor(self,window):
        pygame.draw.rect(window, self.color,(self.x,int(self.y),self.sizex,self.sizey))