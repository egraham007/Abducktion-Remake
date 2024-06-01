from Duck import *
from UFO import *
from Formation import *
from Hand import *

class Board:
    mylist = [' '] * 10

    def fillBoard(self):
        index = 0
        for duck in self.mylist:
            if duck == ' ':
                duck1 = UFO.pullDuck()
                self.mylist[index] = duck1
            index += 1

    def get(self, index):
        return self.mylist[index]

    def reset(self):
        self.mylist = [' '] * 10
        self.fillBoard()

    def __str__(self):
        return ('    --1---2---3---4---5--\n' +
                ('    | '+ str(self.mylist[0])+ ' | '+ str(self.mylist[1])+ ' | '+ str(self.mylist[2])+ ' | '+ str(self.mylist[3])+ ' | '+ str(self.mylist[4])+ ' | \n') +
                '    ---------------------\n' +
                ('    | '+ str(self.mylist[9])+ ' | '+ str(self.mylist[8])+ ' | '+ str(self.mylist[7])+ ' | ' + str(self.mylist[6])+ ' | '+ str(self.mylist[5])+ ' | \n') +
                '    -10---9---8---7---6--\n')
    def __repr__(self):
        return self.__str__()