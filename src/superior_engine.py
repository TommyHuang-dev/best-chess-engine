import time
import random
import chess

from constants import piece_constants as pc

class SuperiorEngine:
    def __init__(self, debug = False):
        self.debug = debug
    
    # returns the material difference (positive for engine, negative for other)
    def calc_material_diff(self, board, turn)-> int:
        fen = board.board_fen()
        diff = 0
        for piece in fen:
            if piece.upper() in pc.pv:
                value = pc.pv[piece.upper()]
                if piece.isupper():
                    diff += value
                else:
                    diff -= value
        
        if turn == chess.BLACK:
            return -diff
        return diff

    def play(self, b, turn, timelimit):
        # copy the board to analyze
        board = b.copy()
        
        bestmoves = []
        bestmovesvalue = -100000

        legalmoves = list(board.legal_moves)
        lines = legalmoves
        starttime = time.time()
        while time.time() - starttime < timelimit and len(lines) > 0:
            # evaluate the next line
            nextmove = lines[0]

            board.push(nextmove)
            # get all responses and choose the best one (material wise). If theres a tie add both
            legalresponses = list(board.legal_moves)
            bestresponseval = 100000
            for response in legalresponses:
                board.push(response)
                val = self.calc_material_diff(board, turn)
                if val < bestresponseval:
                    bestresponseval = val
                    bestresponsemove = response

                # reset board
                board.pop()
            
            board.push(bestresponsemove)
            final_diff = self.calc_material_diff(board, turn)

            if final_diff > bestmovesvalue:
                bestmovesvalue = final_diff
                bestmoves = [nextmove]
            elif final_diff == bestmovesvalue:
                bestmoves.append(nextmove)

            # remove
            lines.pop(0)

            # reset board
            board = b.copy()

        return random.choice(bestmoves)
