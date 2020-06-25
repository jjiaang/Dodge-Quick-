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
        self.neg = 1
        self.collision = False
        self.floorValue = 0 # Same value as the player.y value when its on a floor
        self.touchingFloor = False
        self.touchingGround = True
        self.gravCountJump = 25
        self.gravCountFloor = 4
        self.prevJump = False

    # Returns the color of the player
    def getColor(self):

        return self.color

    # Moves left
    def moveLeft(self):

        self.x -= self.speed
    
    # Moves right
    def moveRight(self):

        self.x += self.speed

    # Check to see if it is jumping
    def checkJump(self):

        return self.isJump

    # Player jump command
    def jump(self):

        self.floorValue = 0
        self.prevJump = True

        # Checks to see if jumpCount is >= jumpConstant.
        if (self.jumpCount >= self.jumpConstant):
            self.neg = 1

            # Once it reaches the apex of its jump, neg turns into -1 to bring the player back down
            if self.jumpCount <= 0:
                self.neg = -1
            
            # Speed of the jump
            self.y -= (self.jumpCount**2)*0.025 * self.neg
            self.jumpCount -= 1

            # Checks to see if the player is in the air, if it is, then bring back down. Also checks if the player is touching the ground.
            # Only check if player is still in the air after the jump
            if (self.isJump == False):
                self.checkPlayerY()

            self.touchGround()

            # Check to see if a player is touching a floor
            if self.collision == True and self.floorValue > 0:
                self.y = self.floorValue
                self.collision = False
                self.jumpCount = self.jumpConstant - 1

        else:
            self.isJump = False
            self.jumpCount = -self.jumpConstant
            self.checkPlayerY()

    # Draws the player
    def drawPlayer(self,window):

        pygame.draw.rect(window, self.getColor(),(self.x,int(self.y),self.sizex,self.sizey))

    # Checks to see if the player is in a correct Y position
    def checkPlayerY(self):

        # Upper bound for player cannot leave the screen
        if self.y < 0:
            self.y = 0

        # Check to see if a player is touching a floor
        if self.collision == True and self.floorValue > 0:
            self.y = self.floorValue
            self.collision = False
            self.jumpCount = self.jumpConstant - 1
        
        # Gravity to bring it back down
        if self.y < 580 and self.isJump == False and self.touchingFloor == False:
            self.floorValue = 0

            if self.prevJump == True:
                self.y += (self.gravCountJump**2)*0.025
                if (self.gravCountJump < 28):
                    self.gravCountJump += 1
            
            if self.prevJump == False:
                print(self.gravCountFloor)
                self.y += (self.gravCountFloor**2)*0.025
                if (self.gravCountFloor < 28):
                    self.gravCountFloor += 1

            # Lower bound for the player cannot leave the screen
            if self.y >= 580:
                self.y = 580
                # Check the player touching ground
                self.touchGround()
                self.gravCountFloor = 25

    # Checks to see if the player is touching a floor
    def playerTouchFloor(self,floor):

        if self.y == floor.floorPixelHeight and self.neg == -1:
            self.collision = True
            self.floorValue = floor.floorPixelHeight - floor.width
            self.touchingFloor = True
            self.touchingGround = False
            self.gravCountFloor = 4

    # Checks to see if the player is touching the ground
    def touchGround(self):

        # If the y value of the player is above the ground (aka. less than 580)
        if self.y < 580:
            self.touchingGround = False
        
        if int(self.y) == 580:
            self.touchingGround = True
            self.floorValue = 0
            self.prevJump = False
            self.gravCountFloor = 4

    def isTouchingFloor(self):
        if self.floorValue != self.y:
            self.touchingFloor = False