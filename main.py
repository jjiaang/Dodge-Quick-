import pygame
from Node import Node
from Floor import Floor
from Counter import Counter
import math

pygame.init()
pygame.font.init()

# Set the display accordingly (x,y) and set the title for the game.
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

# Initialize the classes
player = Node(0,580,5)
floor1 = Floor(400,503,20,150)
counter = Counter(750,10)

RUN = True

while RUN:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    # Gets the current key pressed
    keyPressed = pygame.key.get_pressed()

    player.checkPlayerY()

    #Key press event for a
    if keyPressed[pygame.K_a] and player.x > 0:
        player.moveLeft()

    #Key press event for d
    if keyPressed[pygame.K_d] and player.x < 800 - player.sizex:
        player.moveRight()

    #Key press event for space bar
    if not player.checkJump():

        if keyPressed[pygame.K_SPACE] and player.y > 0 and player.y <= 580:
            player.isJump = True

    else:
        player.jump()

    #Checks to see if the player is within the range of the floor.
    if player.x + player.sizex >= floor1.x and player.x <= floor1.x + floor1.length:
        player.playerCollision(floor1.y)
    
    else:
        player.touchingFloor = False


    screen.fill((0,0,0))
    player.drawPlayer(screen)
    floor1.drawFloor(screen)

    # Displays the X and Y position counters
    counter.printXPOS(screen,player)
    counter.printYPOS(screen,player)

    pygame.display.update()