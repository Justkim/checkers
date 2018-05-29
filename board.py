import copy
from random import shuffle
class board(object):

    turn=1


    def __init__(self,tiles):
       self.tiles=tiles








    def printBoard(self):
        for i in self.tiles:
            for j in i:
                print (j,end=' ')


            print()
            
    def isGameOver(self):


        whitegameOverFlag=True
        blackgameOverFlag=True

        for i in self.tiles:
            if(i.count('W') != 0 or i.count('KW') != 0):
                #print("yay")
                whitegameOverFlag=False
            if (i.count('B') != 0 or i.count('KB') != 0):
                blackgameOverFlag = False
        print(whitegameOverFlag)
        print(blackgameOverFlag)
        if(whitegameOverFlag):
            return 1
        if(blackgameOverFlag):
            return 2
        else:
            return 0



    def calculateMove(self,turn):

        moves=[]
        if(turn is 1):
            piece='W'
            kingpiece='KW'
        elif(turn is 2):
            piece = 'B'
            kingpiece = 'KB'

        blank='-'


        #aval check kon age khone haye orib atrafet khalie mituni ber
        #age por bud check kon harif bashe
        #age harif bud bebin badish khalie? age are az rush bepar o hazfesh kon!
        #row+-1 col+-1
        #row az 0 ta 7 col az 0 ta 7 mojaze
        currentBoard=self.tiles
        #print("DOING SOME SHIT FOR TURN"+str(turn))

        for i in range(0,8):
            for j in range(0,8):


                #i is our row
                if(turn is 1 or self.tiles[i][j]==kingpiece):

                    if(self.tiles[i][j] == piece or self.tiles[i][j]==kingpiece):
                        if(j+1<8 and i+1<8):
                            #lets move down right
                            if(self.tiles[i+1][j+1] != piece and self.tiles[i+1][j+1] != kingpiece):

                                if(self.tiles[i+1][j+1] == blank):
                                    temp = copy.deepcopy(currentBoard)
                                    if(i+1==7 or self.tiles[i][j]==kingpiece):
                                        temp[i + 1][j + 1] = kingpiece
                                    else:
                                        temp[i + 1][j + 1] = piece



                                    temp[i][j]='-'
                                    newBoard = board(temp)
                                    moves.append(newBoard)
                                    #print("I made something and piece"+" "+str(i)+" "+str(j))
                                    #print(temp)
                                    temp=[]

                                elif (i + 2 < 8  and j + 2 < 8):  # yay! enemy is here
                                    if(self.tiles[i+2][j+2] == blank):
                                        temp=copy.deepcopy(currentBoard)
                                        if (i+2 == 7 or self.tiles[i][j]==kingpiece):

                                            temp[i + 2][j + 2] = kingpiece
                                        else:
                                            temp[i + 2][j + 2] = piece
                                        temp[i + 1][j + 1]='-'

                                        temp[i][j] = '-'
                                        newBoard = board(temp)
                                        moves.append(newBoard)
                                        #print("I made something and piece"+" "+str(i)+" "+str(j))
                                        #print(temp)
                                         
                                        temp=[]

                        if (j - 1 >=0 and i + 1 < 8):
                            # lets move down left
                            if (self.tiles[i + 1][j - 1] != piece and self.tiles[i + 1][j - 1] != kingpiece):
                                if (self.tiles[i + 1][j - 1] == blank):
                                    temp=copy.deepcopy(currentBoard)
                                    if(i+1==7 or self.tiles[i][j]==kingpiece):
                                        temp[i + 1][j - 1] = kingpiece
                                    else:
                                        temp[i + 1][j - 1] = piece

                                    temp[i][j] = '-'
                                    newBoard = board(temp)
                                    moves.append(newBoard)
                                    #print("I made something and piece"+" "+str(i)+" "+str(j))
                                    #print(temp)
                                     
                                    temp=[]


                                elif (i + 2 < 8 and j - 2 >= 8):  # yay! enemy is here
                                    if (self.tiles[i + 2][j - 2] == blank):
                                        temp=copy.deepcopy(currentBoard)
                                        if (i+2 == 7 or self.tiles[i][j]==kingpiece):

                                            temp[i + 2][j - 2] = kingpiece
                                        else:
                                            temp[i + 2][j - 2] = piece
                                        temp[i + 1][j - 1] = '-'

                                        temp[i][j] = '-'
                                        newBoard = board(temp)
                                        moves.append(newBoard)
                                        #print("I made something and piece"+" "+str(i)+" "+str(j))
                                        #print(temp)
                                         
                                        temp=[]

                if(turn is 2 or self.tiles[i][j]==kingpiece):
                    if (self.tiles[i][j] == piece or self.tiles[i][j] == kingpiece):
                        if (j + 1 < 8 and i - 1 >=0):
                            # lets move up right
                            if (self.tiles[i - 1][j + 1] != piece and self.tiles[i - 1][j + 1] != kingpiece):
                                if (self.tiles[i - 1][j + 1] == blank):
                                    temp=copy.deepcopy(currentBoard)
                                    if(i-1==0 or self.tiles[i][j]==kingpiece):
                                        temp[i - 1][j + 1] = kingpiece
                                    else:
                                        temp[i - 1][j + 1] = piece

                                    temp[i][j] = '-'
                                    newBoard = board(temp)
                                    moves.append(newBoard)
                                    #print("I made something and piece"+" "+str(i)+" "+str(j))
                                    #print(temp)
                                     
                                    temp=[]

                                elif(i-2>=0 and j+2<8):#yay! enemy is here
                                    if (self.tiles[i - 2][j + 2] == blank):
                                        temp=copy.deepcopy(currentBoard)
                                        if (i-2 == 0 or self.tiles[i][j]==kingpiece):

                                            temp[i - 2][j + 2] = kingpiece
                                        else:
                                            temp[i - 2][j + 2] = piece
                                        temp[i - 1][j + 1] = '-'

                                        temp[i][j] = '-'
                                        newBoard = board(temp)
                                        moves.append(newBoard)
                                        #print("I made something and piece"+" "+str(i)+" "+str(j))
                                        #print(temp)
                                         
                                        temp=[]

                        if (j - 1 >= 0 and i - 1 >= 0):
                            # lets move up left

                            if (self.tiles[i - 1][j - 1] != piece and self.tiles[i - 1][j - 1] != kingpiece):
                                if (self.tiles[i - 1][j - 1] == blank):
                                    
                                    temp=copy.deepcopy(currentBoard)
                                    if (i-1 == 0 or self.tiles[i][j]==kingpiece):
                                        temp[i - 1][j - 1] = kingpiece
                                    else:
                                        temp[i - 1][j -1 ] = piece

                                    temp[i][j] = '-'
                                    newBoard = board(temp)
                                    moves.append(newBoard)
                                    #print("I made something and piece"+" "+str(i)+" "+str(j))
                                    #print(temp)
                                     
                                    temp=[]


                                elif (i - 2 >= 0 and j - 2 < 8):  # yay! enemy is here
                                    if (self.tiles[i - 2][j - 2] == blank):
                                        temp=copy.deepcopy(currentBoard)
                                        if (i-2 == 0 or self.tiles[i][j]==kingpiece):

                                            temp[i - 2][j - 2] = kingpiece
                                        else:
                                            temp[i - 2][j - 2] = piece
                                        temp[i - 1][j - 1] = '-'

                                        temp[i][j] = '-'
                                        newBoard = board(temp)
                                        moves.append(newBoard)
                                        #print("I made something and piece"+" "+str(i)+" "+str(j))
                                        #print(temp)
                                         
                                        temp=[]

        shuffle(moves)

        return moves


    def getWhiteScore(self):
        score=0
        for i in range(0,8):
            for j in range(0,8):
                if(self.tiles[i][j] is 'W'):
                    score=score+5
                elif (self.tiles[i][j] is 'KW'):
                    score = score + 10
                if (self.tiles[i][j] is 'B'):
                    score = score - 15
                elif (self.tiles[i][j] is 'KB'):
                    score = score - 20

        return score

    def getBlackScore(self):
        score = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if (self.tiles[i][j] is 'B'):
                    score = score + 5
                elif (self.tiles[i][j] is 'KB'):
                    score = score + 10
                if (self.tiles[i][j] is 'W'):
                     score = score - 15
                elif (self.tiles[i][j] is 'KW'):
                     score = score - 20

        return score























