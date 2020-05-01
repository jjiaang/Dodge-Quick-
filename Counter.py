import pygame

pygame.init()

pygame.font.init()

class Counter():

    def __init__(self,xpos,ypos):
        self.x = xpos
        self.y = ypos

        self.newFont = pygame.font.SysFont("Arial",12)

    # Displays the X position counter
    def printXPOS(self,window,player):
        text = self.newFont.render("x = " + str(int(player.x)),1,(255,255,255))
        window.blit(text,(self.x,self.y))

    # Displays the Y position counter
    def printYPOS(self,window,player):
        text = self.newFont.render("y = " + str(int(player.y)),1,(255,255,255))
        window.blit(text,(self.x,self.y+15))