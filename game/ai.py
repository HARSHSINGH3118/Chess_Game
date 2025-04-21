from tkinter import messagebox

class AIModule:
    def __init__(self, game):
        self.game = game

    def system_king_move(self):
        sr, sc = self.game.board.find_piece("SK")
        if sr == -1:
            return

        best_score = float('-inf')
        best_move = None

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                orig_piece = self.game.board.grid[nr][nc]
                self.game.board.grid[sr][sc] = ""
                self.game.board.grid[nr][nc] = "SK"

                score = self.minimax(depth=1, is_max=False)

                self.game.board.grid[sr][sc] = "SK"
                self.game.board.grid[nr][nc] = orig_piece

                if score > best_score:
                    best_score = score
                    best_move = (nr, nc)

        if best_move:
            nr, nc = best_move
            if self.game.board.grid[nr][nc] == "UK":
                self.game.points -= 100
                self.game.board.move(sr, sc, nr, nc)
                self.game.draw_board()
                messagebox.showwarning("Game Over", "Your King was killed! -100 points")
                self.game.root.after(500, self.game.root.destroy)
                return
            elif self.game.board.grid[nr][nc] == "UB":
                messagebox.showinfo("Alert", "System King destroyed your Boat!")

            self.game.board.move(sr, sc, nr, nc)

    def minimax(self, depth, is_max):
        if depth == 0:
            return self.evaluate_board()

        if is_max:
            max_eval = float('-inf')
            sr, sc = self.game.board.find_piece("SK")
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nr, nc = sr + dr, sc + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    orig_piece = self.game.board.grid[nr][nc]
                    self.game.board.grid[sr][sc] = ""
                    self.game.board.grid[nr][nc] = "SK"
                    eval_score = self.minimax(depth - 1, False)
                    self.game.board.grid[sr][sc] = "SK"
                    self.game.board.grid[nr][nc] = orig_piece
                    max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(8):
                for j in range(8):
                    if self.game.board.grid[i][j] in ["UK", "UB"]:
                        moves = self.game.logic.get_valid_moves(i, j)
                        for (ni, nj) in moves:
                            orig_piece = self.game.board.grid[ni][nj]
                            self.game.board.grid[ni][nj] = self.game.board.grid[i][j]
                            self.game.board.grid[i][j] = ""
                            eval_score = self.minimax(depth - 1, True)
                            self.game.board.grid[i][j] = self.game.board.grid[ni][nj]
                            self.game.board.grid[ni][nj] = orig_piece
                            min_eval = min(min_eval, eval_score)
            return min_eval

    def evaluate_board(self):
        uk = self.game.board.find_piece("UK")
        ub = self.game.board.find_piece("UB")
        sk = self.game.board.find_piece("SK")

        if sk == (-1, -1):
            return -1000
        if uk == (-1, -1):
            return 1000

        score = 0
        if uk != (-1, -1):
            score -= 2 * (abs(sk[0] - uk[0]) + abs(sk[1] - uk[1]))
        if ub != (-1, -1):
            score -= abs(sk[0] - ub[0]) + abs(sk[1] - ub[1])
        return score
