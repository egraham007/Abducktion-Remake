from Board import *
from Hand import *
from UFO import *
from Duck import *
from Formation import *

class MainGame:
    print("")
    print("Welcome to Abducktion! This is a game created by Evan Graham based on the real Abducktion Game.")
    print("Have fun and try to get the highest score possible! Use your ducks wisely and "
          "maneuver them through their ponds.")
    print("   - You will be prompted to complete formations of ducks of the same colors")
    print("   - Use a swap or a replace by plugging in two numbers next to another or enter one number followed by the "
          "letter 'R'")
    print("   - There are four formations which you can get, J, T, L and I")
    print("   - Formations are based on the classic tetris representations of groups of four ducks. Enjoy!")
    board = Board()
    board.fillBoard()
    form = Formation()
    print("")
    form.form()
    print(board)
    print("You have 100 moves, use them wisely to complete the most formations possible.")
    hand = Hand()
    turn = Turn()
    hand.move(board, form, turn)


if __name__ == "__main__":
    maingame = MainGame()