
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
            scores.append(self.scoreBoard(Board))
        return scores
    def highScores(self,scores):
        k=[]
        b=0
        for i in range(0,scores.length):
            if scores[i]>b:
                b=scores[i]
                k=[]
                k.append(i)
            elif scores[i]==b:
                k.append(i)
        return k
    def tiebreakMove(self,board):
        if self.tbt =='LEFT':
            




