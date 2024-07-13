import unittest
from tictactoe import print_board, check_winner, is_board_full, make_move

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Set up a fresh board for each test."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
    

    def test_is_board_full(self):
        """Test if the board is full."""
        self.assertFalse(is_board_full(self.board))  # Board is empty
        self.board = [["X", "O", "X"],
                      ["X", "O", "O"],
                      ["O", "X", "X"]]
        self.assertTrue(is_board_full(self.board))  # Board is full
    
    def test_make_move(self):
        """Test making a valid move."""
        self.assertTrue(make_move(self.board, 0, 0, "X"))
        self.assertEqual(self.board[0][0], "X")
        self.assertFalse(make_move(self.board, 0, 0, "O"))  # Cell already occupied

    def test_check_winner_rows(self):
        """Test winning condition in rows."""
        self.board[0] = ["X", "X", "X"]
        self.assertEqual(check_winner(self.board), "X")
        self.board[1] = ["O", "O", "O"]
        self.assertEqual(check_winner(self.board), "O")

    


if __name__ == "__main__":
    unittest.main()
