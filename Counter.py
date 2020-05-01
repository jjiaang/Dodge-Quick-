import pygame

pygame.init()

pygame.font.init()

class Counter():

    def __init__(self,xpos,ypos):
        self.x = xpos
        self.y = ypos

        self.newFont = pygame.font.SysFont("Arial",10)

    def printXPOS(self,window,player):
        text = self.newFont.render("x = " + str(float(player.x)),1,(255,255,255))
        window.blit(text,(self.x,self.y))