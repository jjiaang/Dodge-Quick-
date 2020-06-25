import pygame
from Node import Node
from Floor import Floor
from Counter import Counter
import math
import random

class Game():

    def __init__(self):

        pygame.init()
        pygame.font.init()

        # Set the display accordingly (x,y) and set the title for the game.
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")

        # Initialize the classes
        self.player = Node(0,580,5)
        self.floors = [Floor(300,0,20,150)]
        self.counter = Counter(750,10)

        self.RUN = True

    def startGame(self):

        while self.RUN:
            pygame.time.delay(12)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUN = False

            # Gets the current key pressed
            keyPressed = pygame.key.get_pressed()

            #Key press event for a
            if keyPressed[pygame.K_a] and self.player.x > 0:
                self.player.moveLeft()

            self.player.checkPlayerY()

            if self.floors[0].x < 600 and self.floors[0].keepMoving == False:
                self.floors[0].x += 1
            else:
                self.floors[0].x -= 1
                self.floors[0].keepMoving = True
                if self.floors[0].x < 150:
                    self.floors[0].keepMoving = False

            #Key press event for d
            if keyPressed[pygame.K_d] and self.player.x < 800 - self.player.sizex:
                self.player.moveRight()

            #Key press event for space bar
            if not self.player.checkJump():

                # Can only jump if the player is touching the ground or touching a floor.
                if (keyPressed[pygame.K_SPACE] and self.player.y > 0 and self.player.y <= 580 and self.player.touchingGround == True) or (keyPressed[pygame.K_SPACE] and self.player.y > 0 and self.player.y <= 580 and self.player.touchingFloor == True):
                    self.player.isJump = True

            else:
                self.player.jump()

            #Checks to see if the player is within the range of the floors.
            #If the player is touching the floor, we set prevJump to false, since, that way, the gravity changes for the player
            #If prevJump is false, then the player will start falling as if it were falling from the apex of a jump, rather than having a constant value, which is super fast
            for floor in self.floors:
                currentFloor = floor

                if self.player.x + self.player.sizex >= floor.x and self.player.x <= floor.x + floor.length:
                    self.player.playerTouchFloor(floor)
                    if self.player.touchingFloor:
                        self.player.prevJump = False
                    break
            
            #Checks to see if the player is not touching a floor anymore, based on the currentFloor, since floors cannot overlap, and a player can only touch one floor
            if self.player.x + self.player.sizex < currentFloor.x or self.player.x > currentFloor.x + currentFloor.length:
                self.player.touchingFloor = False

            print(self.player.y)    

            self.screen.fill((0,0,0))
            self.player.drawPlayer(self.screen)
            for floor in self.floors:
                floor.drawFloor(self.screen)

            #print("Player y ",self.player.y,"Player x ", int(self.player.x), "Floor value ",self.player.floorValue,self.player.touchingFloor,self.player.isJump)

            # Displays the X and Y position counters
            self.counter.printXPOS(self.screen,self.player)
            self.counter.printYPOS(self.screen,self.player)

            pygame.display.update()