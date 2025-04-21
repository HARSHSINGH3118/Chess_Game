class Board:
    def __init__(self):
        self.grid = [["" for _ in range(8)] for _ in range(8)]

    def place_initial_pieces(self):
        self.grid[7][4] = "UK"
        self.grid[7][0] = "UB"
        self.grid[0][4] = "SK"

    def move(self, r1, c1, r2, c2):
        self.grid[r2][c2] = self.grid[r1][c1]
        self.grid[r1][c1] = ""

    def find_piece(self, name):
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == name:
                    return (i, j)
        return (-1, -1)
