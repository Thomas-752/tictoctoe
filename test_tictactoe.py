import unittest
from tictactoe import print_board, check_winner, is_board_full, make_move

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Set up a fresh board for each test."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]

if __name__ == "__main__":
    unittest.main()
