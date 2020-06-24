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
        self.floors = [Floor(300,random.randrange(0,24),20,150)]
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

            self.player.checkPlayerY()

            #Key press event for a
            if keyPressed[pygame.K_a] and self.player.x > 0:
                self.player.moveLeft()

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

            #Checks to see if the player is within the range of the floor1.
            for floor in self.floors:
                if self.player.x + self.player.sizex >= floor.x and self.player.x <= floor.x + floor.length:
                    self.player.playerTouchFloor(floor)
                
                else:
                    self.player.touchingFloor = False


            self.screen.fill((0,0,0))
            self.player.drawPlayer(self.screen)
            for floor in self.floors:
                floor.drawFloor(self.screen)

            print(int(self.player.y),self.player.floorValue)

            # Displays the X and Y position counters
            self.counter.printXPOS(self.screen,self.player)
            self.counter.printYPOS(self.screen,self.player)

            pygame.display.update()