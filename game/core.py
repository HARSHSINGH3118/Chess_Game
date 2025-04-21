import os
import tkinter as tk
from tkinter import messagebox
from config import CELL_SIZE, BOARD_SIZE
from game.board import Board
from game.pieces import PieceLogic
from game.ai import AIModule

# Correct path to assets
ASSETS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game - King vs King & Boat")
        self.canvas = tk.Canvas(root, width=CELL_SIZE * BOARD_SIZE, height=CELL_SIZE * BOARD_SIZE)
        self.canvas.pack()

        self.images = {
            "UK": tk.PhotoImage(file=os.path.join(ASSETS_PATH, "user_king.png")).subsample(6, 6),
            "UB": tk.PhotoImage(file=os.path.join(ASSETS_PATH, "user_boat.png")).subsample(6, 6),
            "SK": tk.PhotoImage(file=os.path.join(ASSETS_PATH, "system_king.png")).subsample(6, 6)
        }

        self.points = 1000
        self.selected_piece = None
        self.valid_moves = []
        self.board = Board()
        self.logic = PieceLogic(self.board)
        self.ai = AIModule(self)

        self.board.place_initial_pieces()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)

        self.status_label = tk.Label(root, text=f"Points: {self.points}", font=("Arial", 14))
        self.status_label.pack()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = "#ffffff" if (row + col) % 2 == 0 else "#1a1a1a"
                outline = "#cccccc" if (row + col) % 2 == 0 else "#333333"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline)

                if (row, col) in self.valid_moves:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=3)

                piece = self.board.grid[row][col]
                if piece:
                    img = self.images.get(piece)
                    if img:
                        self.canvas.create_image(x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2, image=img)

    def on_click(self, event):
        row = event.y // CELL_SIZE
        col = event.x // CELL_SIZE

        if self.selected_piece:
            sel_row, sel_col = self.selected_piece
            piece = self.board.grid[sel_row][sel_col]

            if (row, col) in self.valid_moves:
                if self.board.grid[row][col] in ["UK", "UB"]:
                    return

                target = self.board.grid[row][col]
                if piece == "UK":
                    self.points -= 10
                elif piece == "UB":
                    self.points -= 20

                if target == "SK":
                    self.points += 100
                    self.board.move(sel_row, sel_col, row, col)
                    self.draw_board()
                    self.status_label.config(text=f"Points: {self.points}")
                    messagebox.showinfo("You Win!", f"🎉 You killed the System King!\nFinal Score: {self.points}")
                    self.root.destroy()
                    return

                self.board.move(sel_row, sel_col, row, col)
                self.selected_piece = None
                self.valid_moves = []
                self.ai.system_king_move()
                self.check_user_king_loss()
                self.draw_board()
                self.status_label.config(text=f"Points: {self.points}")
            else:
                self.selected_piece = None
                self.valid_moves = []
                self.draw_board()
        else:
            if self.board.grid[row][col] in ["UK", "UB"]:
                self.selected_piece = (row, col)
                self.valid_moves = self.logic.get_valid_moves(row, col)
                self.draw_board()

    def check_user_king_loss(self):
        if self.board.find_piece("UK") == (-1, -1):
            messagebox.showinfo("Game Over", f"Your King is dead. Final Points: {self.points}")
            self.root.destroy()
