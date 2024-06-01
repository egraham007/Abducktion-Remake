from Board import *
import random

class Formation:
    def form(self):
        self.formlist = ["J", "L", "T", "I"]
        random.shuffle(self.formlist)
        self.myform = self.formlist[0]
        print('Your formation is:', self.myform)

    def isFormComplete(self, board):
        if self.myform == 'J' and self.isJ(board):
            return True
        if self.myform == 'L' and self.isL(board):
            return True
        if self.myform == 'T' and self.isT(board):
            return True
        if self.myform == 'I' and self.isI(board):
            return True
        return False
    
    def isJ(self, board):
        return self.ducksMatch(board.get(0), board.get(1), board.get(2), board.get(7)) or self.ducksMatch(board.get(1), board.get(2), board.get(3),
            board.get(6)) or self.ducksMatch(board.get(2), board.get(3), board.get(4), board.get(5)) or self.ducksMatch(board.get(5), board.get(6),
            board.get(7), board.get(2)) or self.ducksMatch(board.get(6), board.get(7), board.get(8), board.get(1)) or self.ducksMatch(board.get(7),
            board.get(8), board.get(9), board.get(0))
    def isL(self, board):
        return self.ducksMatch(board.get(0), board.get(1), board.get(2), board.get(9)) or self.ducksMatch(board.get(3), board.get(1), board.get(2),
            board.get(8)) or self.ducksMatch(board.get(4), board.get(3), board.get(2), board.get(7)) or self.ducksMatch(board.get(9), board.get(7),
            board.get(2), board.get(8)) or self.ducksMatch(board.get(6), board.get(7), board.get(3), board.get(8)) or self.ducksMatch(board.get(7),
            board.get(6), board.get(5), board.get(4))
    def isT(self, board):
        return self.ducksMatch(board.get(0), board.get(1), board.get(2), board.get(8)) or self.ducksMatch(board.get(1), board.get(2), board.get(3),
            board.get(7)) or self.ducksMatch(board.get(2), board.get(3), board.get(4), board.get(6)) or self.ducksMatch(board.get(9), board.get(8),
            board.get(7), board.get(1)) or self.ducksMatch(board.get(8), board.get(7), board.get(6), board.get(2)) or self.ducksMatch(board.get(7),
            board.get(6), board.get(5), board.get(3))
    def isI(self, board):
        return self.ducksMatch(board.get(0), board.get(1), board.get(2), board.get(3)) or self.ducksMatch(board.get(3), board.get(1), board.get(2),
            board.get(4)) or self.ducksMatch(board.get(5), board.get(6), board.get(7), board.get(8)) or self.ducksMatch(board.get(9), board.get(8),
            board.get(7), board.get(6))
    def ducksMatch(self, duck1, duck2, duck3, duck4):
        return duck1.getColor() == duck2.getColor() == duck3.getColor() == duck4.getColor()