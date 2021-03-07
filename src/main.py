import chess
import sys

# setup
board = chess.Board()

if len(sys.argv) > 1 and sys.argv[1] == "black":
    playerToMove = False
    playerColour = "black"
else:
    playerToMove = True
    playerColour = "white"
    

while not board.is_game_over(claim_draw=True):
    # since we use darktheme, gotta invert colours when playing as white
    print("----------------")
    print(board.unicode(invert_color = playerColour == "white"))

    while playerToMove:
        nextMove = input()
        if nextMove == "u":
            try:
                board.pop()
                playerToMove = False
            except ValueError:
                print("cannot takeback further")
        else:
            try:
                board.push_san(nextMove)
                playerToMove = False
            except ValueError:
                print("invalid move you suck")
    
    # engine moves

    playerToMove = True

print("GAME OVER!!!")
print(board.result(claim_draw=True))
