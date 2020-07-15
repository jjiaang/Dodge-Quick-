import pygame
from Node import Node
from Floor import Floor
from Counter import Counter
from Key import Key

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

        self.gameOver = False

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

            # Checks to see if the player has hit a key
            if self.player.hitKey(self.key):
                self.playerFoundKey = True

            # Checks to see if the player is within a range, if the floor is at the end, floorTurn is changed
            # The boolean value of floorTurn controls the floor movement
            for floor in self.floors:
                if self.player.detectCollision(floor):
                    self.player.color = (255,0,0)
                    self.gameOver = True
                    self.RUN = False

                if floor.x < 800 - floor.length and not floor.floorTurn:
                    floor.direction = 1
                    floor.x += floor.velocity
                else:
                    floor.direction = -1
                    floor.x += floor.velocity * floor.direction
                    floor.floorTurn = True
                    if floor.x < 0:
                        floor.floorTurn = False

            #Key press event for d
            if keyPressed[pygame.K_d] and self.player.x < 800 - self.player.sizex:
                self.player.moveRight()

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