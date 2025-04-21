# ♟️ Chess Game – King vs King & Boat

A fun and simplified chess-inspired Python game using `tkinter`, where you play as a **User King (UK)** and **User Boat (UB)** against a **System King (SK)** controlled by a basic AI with minimax strategy.

## 🎮 Gameplay Overview

- The board is 8x8.
- You control:
  - **UK (User King)** – moves one step in any direction.
  - **UB (User Boat)** – moves in straight lines (like a rook), cannot jump over pieces.
- The opponent:
  - **SK (System King)** – controlled by the AI, uses minimax strategy to chase your King or destroy your Boat.
- **Scoring**:
  - Move UK → -10 points
  - Move UB → -20 points
  - Kill SK → +100 points
  - If SK kills UK → -100 points and Game Over
  - If SK kills UB → Warning only

## 🧠 AI Logic

- The AI uses a depth-1 minimax algorithm to move the System King (SK).
- It prioritizes capturing the UK or getting closer to it.

## 📦 Features

- Turn-based play with mouse clicks.
- Simple score-based win/lose mechanics.
- Message alerts for major events.
- AI responds after every user move.
- Clean visual board using `tkinter` with image assets.

 
## 🚀 How to Run

1. Clone the repository.
2. Make sure you have **Python 3** installed.
3. Place image assets in the `assets/` folder with correct names:
   - `user_king.png`
   - `user_boat.png`
   - `system_king.png`
4. Run the game:

```bash
python main.py
```
🔧 Requirements
Python 3.x

tkinter (standard in most Python distributions)

📝 Rules Recap
UK can move 1 cell in any direction.

UB can move in straight lines, cannot jump over other pieces.

SK uses minimax to decide best move.

Game ends if your King dies or you kill the System King.

 
![{406FEC59-BDC2-4CBA-A412-B32D5BD898FE}](https://github.com/user-attachments/assets/ab706dfd-c52d-480d-820c-b99d45b7ab1e)


📄 License
Open source project for learning purposes. Use freely!Just Mention the  Credit  to Harsh Singh

