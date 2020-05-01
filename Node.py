import pygame

pygame.init()

class Node():

    def __init__(self, x, y,speed):
        self.x = x
        self.y = y
        self.color = (255,255,0)
        self.speed = speed
        self.sizex = 20
        self.sizey = 20
        self.isJump = False
        self.jumpCount = 25
        self.jumpConstant = -25

    def getColor(self):
        return self.color

    def moveLeft(self):
        self.x -= self.speed
    
    def moveRight(self):
        self.x += self.speed

    def checkJump(self):
        return self.isJump

    def jump(self):
        if self.jumpCount >= self.jumpConstant:
            neg = 1
            if self.jumpCount < 0:
                neg = -1
            self.y -= (self.jumpCount**2)*0.025 * neg
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = -self.jumpConstant

    def drawPlayer(self,window):
        pygame.draw.rect(window, self.getColor(),(self.x,int(self.y),self.sizex,self.sizey))
