import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from Game import Game

def main():
    while (1): 
        
        newGame = Game()

        newGame.startGame()

        if newGame.gameOver and not newGame.RUN:
            newGame.startGame()
        else:
            break

if __name__ == "__main__":  
    main()