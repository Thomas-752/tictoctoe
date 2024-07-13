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


if __name__ == "__main__":
    unittest.main()
