import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QFont

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

        self.current_player = "X"
        self.board = [""] * 9

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.buttons = []

        grid_layout = QGridLayout()
        i = 1
        for row in range(3):
            button_row = []
            for col in range(3):        
                button = QPushButton(f"{i}", self)
                i += 1
                button.setMinimumSize(100, 100)
                button.setFont(QFont("Arial", 20))
                button.clicked.connect(self.make_button_click_handler(row, col))
                button_row.append(button)
                grid_layout.addWidget(button, row, col)
            self.buttons.append(button_row)

        layout.addLayout(grid_layout)

    def make_button_click_handler(self, row, col):
        def handler():
            self.on_button_click(row, col)
        return handler

    def on_button_click(self, row, col):
        index = row * 3 + col

        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[row][col].setText(self.current_player)

            if self.check_winner():
                self.show_winner()
                self.reset_board()
            elif len(set(board)) == 2:
                self.show_draw()
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True

        return False

    def show_winner(self):
        winner = f"Player {self.current_player} wins!"
        # Create a QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Winner!")
        msg_box.setText(winner)
        msg_box.setIcon(QMessageBox.Information)

        # Set the modal property to make the dialog modal
        msg_box.setModal(True)

        # Show the dialog and wait for the user's response
        result = msg_box.exec_()

    
    def show_draw(self):
        # Create a QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("It's a draw!")
        msg_box.setText("Better luck next time!")
        msg_box.setIcon(QMessageBox.Information)

        # Set the modal property to make the dialog modal
        msg_box.setModal(True)

        # Show the dialog and wait for the user's response
        result = msg_box.exec_()

    

    def reset_board(self):
        i = 1 
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText(f"{i}")
                i += 1
        self.board = [""] * 9
        self.current_player = "X"
        self.setWindowTitle("Tic Tac Toe")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
