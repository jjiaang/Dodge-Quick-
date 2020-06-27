import pygame
from Node import Node
from Floor import Floor
from Counter import Counter
from Key import Key
import math
import random

"""
2020-06-27
Abandon all ideas of a platformer jumping game, instead make it so that the player has to move up the screen to dodge floors, get a key, and come back and unlock the door
"""

class Game():

    def __init__(self):

        # Initialize pygame for the game class, as well as initializing the font.
        pygame.init()
        pygame.font.init()

        # Set the display accordingly (x,y) and set the title for the game.
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")

        # Initialize the classes
        self.player = Node(0,580,5)
        self.key = Key(680,0)
        #Current floor values are probably going to be level 1
        self.floors = [Floor(300,0,20,50),Floor(500,1,20,50),Floor(100,2,20,50),Floor(200,3,20,50),Floor(400,4,20,50), Floor(250,5,20,50),Floor(50,6,20,50),Floor(150,7,20,50),Floor(550,8,20,50),Floor(450,9,20,50)]
        self.counter = Counter(750,10)

        self.RUN = True

        self.playerFoundKey = False

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
                
            #Key press event for w
            if keyPressed[pygame.K_w] and self.player.y > 0:
                self.player.moveUp()

            #Key press event for w
            if keyPressed[pygame.K_s] and self.player.y >= 0:
                if self.player.y < 580:
                    self.player.moveDown()

            #self.player.checkPlayerY()

            if self.player.hitKey(self.key):
                self.playerFoundKey = True

            # Checks to see if the player is within a range, if the floor is at the end, floorTurn is changed
            # The boolean value of floorTurn controls the floor movement
            for floor in self.floors:
                if self.player.detectCollision(floor):
                    self.player.color = (255,0,0)

                if floor.x < 800 - floor.length and not floor.floorTurn:
                    floor.direction = 1
                    floor.x += floor.velocity
                else:
                    floor.direction = -1
                    floor.x += floor.velocity * floor.direction
                    floor.floorTurn = True
                    if floor.x < 0:
                        floor.floorTurn = False

                """
                # Checks to see if the player is on the floor, if the player is on the floor, the player will move with the floor.
                if self.player.touchingFloor:
                    currentFloor = floor
                    self.player.moveWithFloor(currentFloor)
                    break
                """

            #Key press event for d
            if keyPressed[pygame.K_d] and self.player.x < 800 - self.player.sizex:
                self.player.moveRight()

            """
            #Key press event for space bar
            if not self.player.checkJump():

                # Can only jump if the player is touching the ground or touching a floor.
                if (keyPressed[pygame.K_SPACE] and self.player.y > 0 and self.player.y <= 580 and self.player.touchingGround == True) or (keyPressed[pygame.K_SPACE] and self.player.y > 0 and self.player.y <= 580 and self.player.touchingFloor == True):
                    self.player.isJump = True

            else:
                self.player.jump()
            """

            """
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

            """

            # Pygame functions that draw the player and draw the screen, as well as drawing all the floors in the floors dynamic array
            self.screen.fill((0,0,0))
            self.player.drawPlayer(self.screen)

            if not self.playerFoundKey:
                self.key.drawKey(self.screen)
                
            for floor in self.floors:
                floor.drawFloor(self.screen)

            # Displays the X and Y position counters
            self.counter.printXPOS(self.screen,self.player)
            self.counter.printYPOS(self.screen,self.player)

            pygame.display.update()