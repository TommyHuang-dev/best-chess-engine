import chess
import sys
from superior_engine import SuperiorEngine

def invert_board(board : str):
    return "\n".join(board.splitlines()[::-1])

# setup
board = chess.Board()
engine = SuperiorEngine()

if len(sys.argv) > 1 and sys.argv[1] == "black":
    player_to_move = False
    player_colour = "black"
else:
    player_to_move = True
    player_colour = "white"

# time limit for the engine in seconds
engine_time_limit = 2
if len(sys.argv) > 2:
    engine_time_limit = float(sys.argv[2])

while not board.is_game_over(claim_draw=True):
    # since we use darktheme, gotta invert colours when drawing board
    print("----------------")
    if (player_colour == 'black'):
        print(board.unicode(invert_color=True)[::-1])
    else:
        print(board.unicode(invert_color=True))


    if (player_to_move):
        while player_to_move:
            next_move = input()
            if next_move == "u":
                try:
                    board.pop()
                    board.pop()
                    print("----------------")
                    print(board.unicode(invert_color = player_colour == "white"))
                except IndexError:
                    print("cannot takeback further")
            else:
                try:
                    board.push_san(next_move)
                    player_to_move = False
                except ValueError:
                    print("invalid move you suck")
    else:
        result = engine.play(board, time_limit=engine_time_limit)
        board.push(result)
        player_to_move = True

print("GAME OVER!!!")
print(board.result(claim_draw=True))
