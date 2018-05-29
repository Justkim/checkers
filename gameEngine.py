from board import *

class GameEngine:

    def __init__(self,limit):
        self.limit=limit


    def minMax(self,newboard,turn):



        return self.maxMove(newboard,turn,0)

    def maxMove(self,newboard,turn,depth):
       # print("MAX MOVE"+str(turn))


        if (depth >= self.limit):
            return newboard

        bestBoard=None

        if(turn is 1):

            possibleMoves =newboard.calculateMove(1)
            if len(possibleMoves) is 0:
                return newboard
            if(len(possibleMoves) is 0):
                return None


            for i in possibleMoves:

                if len(possibleMoves) is 0:
                    return newboard
                newMove=self.minMove(i,2,depth+1)
                if bestBoard is None or newMove.getWhiteScore()>bestBoard.getWhiteScore():

                    bestBoard=i
            return bestBoard


        elif (turn is 2):
            possibleMoves =newboard.calculateMove(2)
            if len(possibleMoves) is 0:
                return newboard
            for i in possibleMoves:
                newMove = self.minMove(i,1, depth+1)
                if bestBoard is None or newMove.getBlackScore() > bestBoard.getBlackScore():
                    bestBoard = i
            return bestBoard

    def minMove(self,newboard, turn, depth):
        #print("min MOVE" + str(turn))
        if (depth >= self.limit):
            return newboard

        bestBoard = None
        if (turn is 1):
            possibleMoves =newboard.calculateMove(1)
            if len(possibleMoves) is 0:

                return newboard
            for i in possibleMoves:
                newMove = self.maxMove(i, 2, depth+1)
                if bestBoard is None or newMove.getWhiteScore() > bestBoard.getWhiteScore():
                    bestBoard =i
            return bestBoard

        elif (turn is 2):
            possibleMoves =newboard.calculateMove(2)
            if len(possibleMoves) is 0:
                return newboard
            for i in possibleMoves:
                newMove = self.maxMove(i, 1, depth+1)
                if bestBoard is None or newMove.getBlackScore() > bestBoard.getBlackScore():
                    bestBoard = i
            return bestBoard












