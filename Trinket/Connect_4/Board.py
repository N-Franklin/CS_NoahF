from random import randint

class Player:
    def __init__(self, ox, tbt, ply):
        self.ox=ox
        self.tbt=tbt
        self.ply=ply

    def __repr__(self):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    def opp(self):
        if self.ox=='X':
            return 'O'
        elif self.ox=='O':
            return 'X'
    def scoreBoard(self, Board):
        z=self.opp()
        if Board.winsFor(self.ox)==True:
            return 100
        elif Board.winsFor(z)==True:
            return 0
        elif Board.isFull()==True:
            return 1
        else:
            return 50
    def findScore(self,Board):
        scores=[]
        for Col in range(0,Board.width):
            b=Board
            b.addmove(Col,self.ox)
            scores.append(self.scoreBoard(Board))
        return scores
    def highScores(self,scores,board):
        k=[]
        b=0
        for i in range(0,scores.length):
            if scores[i]>b and self.foresight(board,i):
                b=scores[i]
                k=[]

                k.append(i)
            elif scores[i]==b and self.foresight(board,i):
                k.append(i)
        return k

    def tiebreakMove(self,board):
        scores=self.findScore(board)
        high=self.highScores(scores)
        q=len(high)-1
        if self.tbt =='LEFT':
            return high[0]
        elif self.tbt=='RIGHT':
            return high[q]
        else:
            return high[randint(0,q)]

    # checks to see if move will lead to an immediate loss
    def foresight(self,board,c):
        for i in range(0,board.width):
            l = board.addMove(self, c, self.ox)
            l.addMove(self,i,self.opp)
            if l.scoreBoard(self)==0:
                return False
        else:
            return True

    def nextMove(self,board):
        return self.tiebreakMove(board)

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width, height ):
        """ the constructor for objects of type Board """

        self.width = width
        self.height = height

        W = self.width
        H = self.height

        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        W = self.width
        H = self.height

        s = ''  # the string to return
        for row in range(0, H):
            s += '|'
            for col in range(0, W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2 * W + 1) * '-'  # bottom of the board
        s += '\n'

        x = -1
        for i in range(W):
            if x == 9:
                x = 0
                s += " " + str(x)
            else:
                x += 1
                s += " " + str(x)

        return s  # the board is complete, return it

    def setBoard(self, moveString):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'  # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'
    def addMove(self,col,ox):
        for i in range(self.height-1,-1,-1):
            if self.data[i][col]==' ':
                self.data[i][col]=ox;break;

    def allowsMove(self,col):
        if 0<col<self.width:
            if self.data[0][col] == ' ':
                return True
        return False
    def isFull(self):
        for i in (0,self.width):
            if self.allowsMove(i):
                return False;
            return True
    def delMove(self,col):
        for i in range(0,self.height,1):
            if self.data[i][col]!= ' ':
                self.data[i][col] = ' ';break;
    def winsFor(self,ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0, H):
            for col in range(0, W - 3):
                if D[row][col] == ox and \
                            D[row][col + 1] == ox and \
                            D[row][col + 2] == ox and \
                            D[row][col + 3] == ox:
                    return True
        for row in range (0,H-3):
            for col in range(0, W):
                if D[row][col] == ox and \
                            D[row+1][col] == ox and \
                            D[row+2][col] == ox and \
                            D[row+3][col] == ox:
                    return True
        for i in range (0,H-3):
            for j in range(0,W-3):
                if D[i][j] == ox and \
                            D[i + 1][j+1] == ox and \
                            D[i + 2][j+2] == ox and \
                            D[i + 3][j+3] == ox:
                    return True
        for row in range(0,H-3):
             for col in range(3,W):
                if D[row][col] == ox and \
                            D[row + 1][col - 1] == ox and \
                            D[row + 2][col - 2] == ox and \
                            D[row + 3][col - 3] == ox:
                    return True
        return False
    def hostGame(self,player):
        x=True
        v=False
        while v==False:
            if x==True:
                print "X's Move"
                c=input(int)
                if self.allowsMove(c):
                    self.addMove(c,'X')
                    v=self.winsFor('X')
                    x=False
            if x==False:
                print "O's Move"
                c=player.tiebreakMove(self)
                if self.allowsMove(c):
                  self.addMove(c,'O')
                  v=self.winsFor('O')
                  x=True
            print self


