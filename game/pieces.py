class PieceLogic:
    def __init__(self, board):
        self.board = board

    def get_valid_moves(self, r1, c1):
        piece = self.board.grid[r1][c1]
        moves = []
        for r2 in range(8):
            for c2 in range(8):
                if self.validate_move(piece, r1, c1, r2, c2):
                    moves.append((r2, c2))
        return moves

    def validate_move(self, piece, r1, c1, r2, c2):
        if r2 < 0 or r2 >= 8 or c2 < 0 or c2 >= 8:
            return False
        if (r1, c1) == (r2, c2):
            return False

        dr = r2 - r1
        dc = c2 - c1

        if piece == "UK":
            return abs(dr) <= 1 and abs(dc) <= 1

        if piece == "UB":
            if dr != 0 and dc != 0:
                return False
            step = 1 if (dr + dc) > 0 else -1
            if dr == 0:
                for c in range(c1 + step, c2, step):
                    if self.board.grid[r1][c] != "":
                        return False
            else:
                for r in range(r1 + step, r2, step):
                    if self.board.grid[r][c1] != "":
                        return False
            return True
        return False
