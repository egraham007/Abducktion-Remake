from Board import *
from Formation import *
from Turn import *
class Hand:
    totalmoves = 0
    movecount = 0
    numForm = 0

    def move(self, board, form, turn):
        response = ' '
        while response != "Q" and response != "q":
            response = input("Your Move. Enter First Pond Number (or 'Q' or 'q' to quit game): ")
            if response == "Q" or response == "q":
                print("Goodbye!")
                exit()
            elif response == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
                response2 = input("Enter Second Pond Number (or 'R' to replace first duck): ")
                if response2 == "R" or response2 == "r":
                    self.replace(response, board)
                elif (response2 == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10"
                      and response2 != response):
                    self.swap(response, response2, board)
                else:
                    print("Incorrect input")
            else:
                print("Incorrect input")
            print(" ")
            self.movecount += 1
            print("This is move #", self.movecount, sep='')
            print(board)
            turn.countdown -= 1
            print("You have", turn.countdown , "moves left. You are trying to form a", form.myform)
            if form.isFormComplete(board) == True:
                self.numForm += 1
                self.totalmoves += self.movecount
                print("You completed a formation! It took", self.movecount, "moves. It's been", self.totalmoves,
                      "total moves with", self.numForm, "formations complete.")
                self.movecount = 0
                board.reset()
                form.form()
                print(board)
            if turn.countdown == 0:
                print("All turns completed. You completed", self.numForm, "formations! Great Job!")
                exit()

    def replace(self, response, board):
        indexresponse = int(response) - 1
        board.mylist[indexresponse] = ' '
        board.fillBoard()

    def swap(self, response, response2, board):
        indexresponse1 = int(response) - 1
        indexresponse2 = int(response2) - 1
        if indexresponse1 + 1 == indexresponse2 or indexresponse1 - 1 == indexresponse2:
            holdval = board.mylist[indexresponse1]
            board.mylist[indexresponse1] = board.mylist[indexresponse2]
            board.mylist[indexresponse2] = holdval
        elif indexresponse1 > indexresponse2:
            vswap = 5 - indexresponse2
            vswap = vswap + 4
            if vswap == indexresponse1:
                holdval = board.mylist[indexresponse1]
                board.mylist[indexresponse1] = board.mylist[indexresponse2]
                board.mylist[indexresponse2] = holdval
        else:
            vswap = 5 - indexresponse1
            vswap = vswap + 4
            if vswap == indexresponse2:
                holdval = board.mylist[indexresponse1]
                board.mylist[indexresponse1] = board.mylist[indexresponse2]
                board.mylist[indexresponse2] = holdval