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
    def addMove(self,col,ox):
        for i in range(self.height-1,-1,-1):
            if self.data[i][col]==' ':
                self.data[i][col]=ox;break;

    def allowsMove(self,col):
        if self.data[0][col] == ' ':
            return True
        else:
            return False
    def isFull(self):
        for i in (0,self.width-1,1):
            if self.allowsMove(i):
                return False;break;
            return True
    def delMove(self,col):
        for i in range(0,self.height-1,1):
            if self.data[i][col]!= ' ':
                self.data[i][col]=' ';break;
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
            for row in range (H-3,0):
                if D[row][col] == ox and \
                                D[row+1][col] == ox and \
                                D[row+2][col] == ox and \
                                D[row+3][col] == ox:
                    return True
            for i in range (H-3,0):
                for j in range(W-3,0):
                    if D[i][j] == ox and \
                                D[i + 1][j+1] == ox and \
                                D[i + 2][j+2] == ox and \
                                D[i + 3][j+3] == ox:
                        return True
            for row in range(H-3,0):
                 for col in range(3,W-1):
                    if D[row][col] == ox and \
                                D[row + 1][col - 1] == ox and \
                                D[row + 2][col - 2] == ox and \
                                D[row + 3][col - 3] == ox:
                        return True
        return False







