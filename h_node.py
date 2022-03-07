
class h_node:
    def __init__(self,current):
        self.current=current
        self.down = []
        self.up = []
        self.left = []
        self.right = []

    def setDownMove(self, move):
        self.down = move

    def setUpMove(self, move):
        self.up = move

    def setLeftMove(self, move):
        self.left = move

    def setRightMove(self, move):
        self.right = move

    def getMoves(self):

        # might be better to add all moves and check for null later

        # moves=[]
        # if(self.down!=[]):
        #     moves.append(self.down)
        # if(self.up!=[]):
        #     moves.append(self.up)
        # if(self.left!=[]):
        #     moves.append(self.left)
        # if(self.right!=[]):
        #     moves.append(self.right)

        # return moves

        return [self.down, self.up, self.left, self.right]

    def __str__(self):
        return "Current:   "+str(self.current)+"\nDown:   "+str(self.down)+"\nUp:    "+str(self.up)+"\nLeft:     "+str(self.left)+"\nRight:   "+str(self.right)
