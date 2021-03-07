import chess
import chess.svg

class SuperiorEngine:
    def __init__(self):
        pass

board = chess.Board()

while not board.is_game_over(claim_draw=True):
    print(board.unicode())

    nextMove = input()
    if nextMove == 'u':
        board.pop()
    else:
        board.push(chess.Move.from_uci(nextMove))

print("GAME OVER!!!")
print(board.result(claim_draw=True))
