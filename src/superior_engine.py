import time

class SuperiorEngine:
    def __init__(self):
        pass

    def play(self, board, time_limit):
        # get copy of move stack

        start_time = time.time()

        while time.time() - start_time < time_limit:
            legalMoves = list(board.legal_moves)
            print(legalMoves[0])
            return legalMoves[0]

        # reset move stack
