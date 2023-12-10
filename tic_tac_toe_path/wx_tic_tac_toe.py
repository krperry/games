"""WX GUI of Tic Tac Toe"""
import wx

class TicTacToe(wx.Frame):
    """Main class representing the Tic Tac Toe game window."""

    def __init__(self):
        """
        Initialize the TicTacToe object.

        Sets up the game window, initializes the game state, and creates the game board.

        Args:
            None
        """
        super().__init__(None, title="Tic Tac Toe", size=(300, 300))
        self.current_player = "X"
        self.board = [" "] * 9

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.buttons = []

        grid_sizer = wx.GridSizer(3, 3, 5, 5)

        i = 1
        for row in range(3):
            button_row = []
            for col in range(3):
                button = wx.Button(panel, label=" ", size=(100, 100))
                button.Bind(wx.EVT_BUTTON, self.make_button_click_handler(row, col))
                button_row.append(button)
                grid_sizer.Add(button, 0, wx.EXPAND)
                i += 1

            self.buttons.append(button_row)

        vbox.Add(grid_sizer, proportion=1, flag=wx.EXPAND)
        panel.SetSizer(vbox)

    def make_button_click_handler(self, row, col):
        """
        Create a button click handler function.

        Args:
            row (int): The row index of the clicked button.
            col (int): The column index of the clicked button.

        Returns:
            function: The button click handler function.
        """
        def handler(event):
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
            self.buttons[row][col].SetLabel(self.current_player)

            if self.check_winner():
                self.show_winner()
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
        dlg = wx.MessageDialog(self, winner, "Winner!", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def ask_play_again(self, title, message):
        """
        Display a message box asking if the players want to play again.

        Args:
            title (str): Title of the message box.
            message (str): Message to be displayed in the message box.

        Returns:
            bool: True if the players want to play again, False otherwise.
        """
        dlg = wx.MessageDialog(self, message, title, wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return result == wx.ID_YES

    def show_draw(self):
        """
        Display a message box announcing a draw.

        Returns:
            None
        """
        dlg = wx.MessageDialog(
            self, "It's a draw!\nBetter luck next time!", "It's a draw!", wx.OK
        )
        dlg.ShowModal()
        dlg.Destroy()

    def reset_board(self):
        """
        Reset the game board.

        Asks players if they want to play again. If yes, the game is reset; otherwise, the window is closed.

        Returns:
            None
        """
        if not self.ask_play_again("Restart Game?", "Do you want to play again?"):
            self.Destroy()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].SetLabel(" ")
        self.board = [" "] * 9
        self.current_player = "X"

if __name__ == "__main__":
    # Start the application and display the Tic Tac Toe game window.
    app = wx.App(False)
    frame = TicTacToe()
    frame.Show(True)
    app.MainLoop()
