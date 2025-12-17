# tictactoe.py

# --- Step 1: Custom Exception ---
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


# --- Step 2: Board Class ---
class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        # Create 3x3 grid with spaces
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    # --- Display Board ---
    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    # --- Make a move ---
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn
        self.last_move = (row, column)

        # Switch turns
        self.turn = "O" if self.turn == "X" else "X"

    # --- Check game status ---
    def whats_next(self):
        # Check for a win
        win = False

        # Rows
        for i in range(3):
            if self.board_array[i][0] != " " and \
               self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                win = True

        # Columns
        for i in range(3):
            if self.board_array[0][i] != " " and \
               self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                win = True

        # Diagonals
        if self.board_array[1][1] != " ":
            if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                win = True
            if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                win = True

        # If win detected
        if win:
            # Note: The current turn has already flipped, so the winner is the opposite player
            winner = "O" if self.turn == "X" else "X"
            return (True, f"{winner} wins!")

        # Check for tie (no empty spaces)
        if all(cell != " " for row in self.board_array for cell in row):
            return (True, "Cat's Game!")

        # Otherwise, continue playing
        return (False, f"{self.turn}'s turn.")


# --- Step 3: Main Game Loop ---
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    board = Board()
    print(board)

    while True:
        game_over, message = board.whats_next()
        if game_over:
            print(message)
            break

        print(message)
        move = input("Enter your move (e.g., 'upper left', 'center', etc.): ")

        try:
            board.move(move)
        except TictactoeException as e:
            print("Error:", e.message)
        print(board)
