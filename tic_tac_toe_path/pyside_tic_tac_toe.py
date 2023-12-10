"""pyside6 GUI of Tic Tac Toe"""
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)

from PySide6.QtGui import QFont


class TicTacToe(QMainWindow):
    """Main class representing the Tic Tac Toe game window."""
    def __init__(self):
        """
        Initialize the TicTacToe object.

        Sets up the game window, initializes the game state, and creates the game board.

        Args:
            None
        """
        super().__init__()

        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

        self.current_player = "X"
        self.board = [" "] * 9

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.buttons = []

        grid_layout = QGridLayout()

        i = 1
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton(" ", self)
                button.setAccessibleDescription(f"{i}")
                i += 1

                button.setMinimumSize(100, 100)
                button.setFont(QFont("Arial", 20))
                button.clicked.connect(self.make_button_click_handler(row, col))
                button_row.append(button)
                grid_layout.addWidget(button, row, col)
            self.buttons.append(button_row)

        layout.addLayout(grid_layout)

    def make_button_click_handler(self, row, col):
        """
        Create a button click handler function.

        Args:
            row (int): The row index of the clicked button.
            col (int): The column index of the clicked button.

        Returns:
            function: The button click handler function.
        """
    
        def handler():
            self.on_button_click(row, col)

        return handler

    def on_button_click(self, row, col):
        """
        Handle button click events.

        Updates the game state when a button is clicked.

        Args:
            row (int): The row index of the clicked button.
            col (int): The column index of the clicked button.

        Returns:
            None
        """
        index = row * 3 + col

        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            self.central_widget.setFocus()
            self.buttons[row][col].setFocus()

            if self.check_winner():
                self.show_winner()
                print("before reset")
                self.reset_board()
            elif " " not in self.board:
                self.show_draw()
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """
        Check for a winning combination on the game board.

        Returns:
            bool: True if there is a winner, False otherwise.
        """
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),  # Rows
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),  # Columns
            (0, 4, 8),
            (2, 4, 6),  # Diagonals
        ]

        for combo in winning_combinations:
            if (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
                != " "
            ):
                return True

        return False

    def show_winner(self):
        """
        Display a message box announcing the winner.

        Returns:
            None
        """
        winner = f"Player {self.current_player} wins!"
        # Create a QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Winner!")
        msg_box.setText(winner)
        #        msg_box.setIcon(QMessageBox.Information)

        # Set the modal property to make the dialog modal
        msg_box.setModal(True)
        msg_box.exec_()

    def ask_play_again(self, title, message):
        """
        Display a message box asking if the players want to play again.

        Args:
            title (str): Title of the message box.
            message (str): Message to be displayed in the message box.

        Returns:
            bool: True if the players want to play again, False otherwise.
        """

    
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        result = msg_box.exec()
        return result == QMessageBox.Yes

    def show_draw(self):
        """
        Display a message box announcing a draw.

        Returns:
            None
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle("It's a draw!")
        msg_box.setText("Better luck next time!")
        # Set the modal property to make the dialog modal
        msg_box.setModal(True)
        msg_box.exec_()

    def reset_board(self):
        """
        Reset the game board.

        Asks players if they want to play again. If yes, the game is reset; otherwise, the window is closed.

        Returns:
            None
        """

        if not self.ask_play_again("Restart Game?", "do you want to play again?"):
            sys.exit()
        i = 1
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText(" ")
                self.buttons[row][col].setAccessibleDescription(f"{i}")
                i += 1
        self.board = [" "] * 9
        self.current_player = "X"
        self.setWindowTitle("Tic Tac Toe")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
