# A Chess Question

## Welcome!

This is a Python program that answers a simple question:  
**Given a board state that the user enters (with 1 white figure and up to 16 black figures), which black figures can the white figure capture?**

---

## 📖 Program Description

1. The program first prompts the user to input a white chess piece and its position on the board.  
   - The user must choose between two predefined piece types: **pawn** or **rook**.
   - The input format must be: (e.g., `pawn a5` or `rook d4`).
   - The program will confirm a successful addition or display an error message if the input is invalid.

2. After the white piece is set, the user is asked to enter the black pieces, one by one, in the same format.  
   - The user must add at least **one** black piece and can add up to **sixteen**.
   - After adding at least one black piece, the user can type **`done`** to stop adding pieces.
   - The program will confirm each successful addition or display an error message for invalid input.

3. The program will validate all inputs:
   - Coordinates must follow the correct format: a letter `a-h` followed by a number `1-8` (e.g., `a1`, `d4`, `h8`).
   - The piece names must be valid (`pawn`, `rook` for the white piece; standard chess pieces for black pieces).
   - Pieces cannot overlap; each square can be occupied by only one piece.
   - Users cannot enter "done" before adding at least one black piece.

4. After all pieces are added, the program will:
   - Display a list of black pieces that the white piece can capture based on **standard chess moves** (e.g., pawns capture diagonally, rooks move horizontally/vertically).
   - If no black pieces can be captured, the program will indicate this clearly.
  
---


## ▶️ How to Run the Program

### Prerequisites

- Python **3.10** or higher (tested with Python **3.13**)

### Instructions

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the program with:

```bash
python chessgame.py
```

### 💡 Example Usage

```bash
Welcome to a chess question game. This program will answer if the placed white chess piece     will be able to take any of the placed black pieces. For this version of the program, you can choose to     play with either a pawn or a rook.

Enter your figure (pawn or rook) and its square (e.g. c6): pawn c6
Successfully added white pawn at c6

Enter coordinates of 1 to 16 black pieces (e.g. pawn a2), or enter 'done' when finished: pawn b7
Successfully added black pawn at b7

Enter coordinates of 1 to 16 black pieces (e.g. pawn a2), or enter 'done' when finished: king d5
Successfully added black king at d5

Enter coordinates of 1 to 16 black pieces (e.g. pawn a2), or enter 'done' when finished: done
All figures successfully placed!

[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
[' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ']
[' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

White piece can take pawn b7
```

## 👩‍💻 Contributor
This project was created by Kristina Rakovskaja.
📬 Connect with me on [LinkedIn](https://www.linkedin.com/in/kristinarakovskaja/)
