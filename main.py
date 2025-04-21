import tkinter as tk
from game.core import ChessGame

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()
