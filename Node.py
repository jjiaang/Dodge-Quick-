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
        self.collision = False
        self.floorValue = 0 # Same value as the player.y value when its on a floor
        self.touchingFloor = False
        self.touchingGround = True

    # Returns the color of the player
    def getColor(self):

        return self.color

    # Moves left
    def moveLeft(self):

        self.x -= self.speed

    def moveUp(self):
        self.y -= self.speed/2

    def moveDown(self):
        self.y += self.speed/2
    
    # Moves right
    def moveRight(self):

        self.x += self.speed

    # Draws the player
    def drawPlayer(self,window):

        pygame.draw.rect(window, self.getColor(),(self.x,int(self.y),self.sizex,self.sizey))

    # Detects if the player has made contact with the floor
    def detectCollision(self,floor):
        if ((self.y <= floor.floorPixelHeight) and (self.y >= floor.floorPixelHeight - floor.width)) and ((self.x > floor.x) and (self.x < floor.x + floor.length)):
            return True
    
    # Detects if the player has hit a key
    def hitKey(self,key):
        if ((self.y >= key.y) and (self.y <= key.y + key.sizey) and (self.x >= key.x) and (self.x <= key.x + key.sizex)):
            return True