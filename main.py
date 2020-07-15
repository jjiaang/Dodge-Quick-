from Game import Game

if __name__ == "__main__":  
    while (1): 
        newGame = Game()

        newGame.startGame()

        if newGame.gameOver and not newGame.RUN:
            newGame.startGame()
        else:
            break