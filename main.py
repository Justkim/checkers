from board import *
from gameEngine import *

tiles = [['-', 'W', '-', 'W', '-', 'W', '-', 'W'], ['W', '-', 'W', '-', 'W', '-', 'W', '-'],
         ['-', 'W', '-', 'W', '-', 'W', '-', 'W']
    , ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'],
         ['B', '-', 'B', '-', 'B', '-', 'B', '-'], ['-', 'B', '-', 'B', '-', 'B', '-', 'B'],
         ['B', '-', 'B', '-', 'B', '-', 'B', '-']]
newBoard = board(tiles)
newBoard.printBoard()
newGame=GameEngine(4)
turn=1
while 1:
    print("in while and turn is"+str(turn))


    newBoard=copy.deepcopy(newGame.minMax(newBoard,turn))
    if newBoard is None:
        print("game over")
        exit()

    if(turn is 1):
        turn =2
    else:
        turn =1
    newBoard.printBoard()
    if(newBoard.isGameOver()):
        break


print("game over")






