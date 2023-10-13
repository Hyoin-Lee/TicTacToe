import unittest
from logic_module import TicTacToeLogic

class TestTicTacToeLogic(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToeLogic()

    def test_initial_board(self):
        expected_board = [[' '] * self.game.board_size for _ in range(self.game.board_size)]
        self.assertEqual(self.game.board, expected_board)

    def test_update_board_valid_move(self):
        player = "X"
        move = 4
        self.assertTrue(self.game.update_board(move, player))
        expected_board = [[' '] * self.game.board_size for _ in range(self.game.board_size)]
        expected_board[move // self.game.board_size][move % self.game.board_size] = 'X'
        self.assertEqual(self.game.board, expected_board)

    def test_update_board_invalid_move(self):
        player = "O"
        move = 4
        self.game.board[move // self.game.board_size][move % self.game.board_size] = "X"
        with self.assertRaises(ValueError):
            self.game.update_board(move, player)
        expected_board = [[' '] * self.game.board_size for _ in range(self.game.board_size)]
        expected_board[move // self.game.board_size][move % self.game.board_size] = 'X'
        self.assertEqual(self.game.board, expected_board)

    def test_check_win_horizontal(self):
        # Test for a horizontal win
        self.game.board = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
        is_win, winner = self.game.check_win()
        self.assertTrue(is_win)
        self.assertEqual(winner, 'X')

    def test_check_win_vertical(self):
        # Test for a vertical win
        self.game.board = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', ' ']]
        is_win, winner = self.game.check_win()
        self.assertTrue(is_win)
        self.assertEqual(winner, 'X')

    def test_check_win_diagonal(self):
        # Test for a diagonal win
        self.game.board = [['X', 'O', ' '], ['O', 'X', ' '], [' ', ' ', 'X']]
        is_win, winner = self.game.check_win()
        self.assertTrue(is_win)
        self.assertEqual(winner, 'X')

    def test_check_tie(self):
        # Test for a tie
        self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertTrue(self.game.check_tie())

        # Test for not a tie
        self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', ' ', 'X']]
        self.assertFalse(self.game.check_tie())

    def test_get_current_player(self):
        # Test for player1 ('X') as the current player
        self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', ' ']]
        self.assertEqual(self.game.get_current_player(), 'X')

        # Test for player2 ('O') as the current player
        self.game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertEqual(self.game.get_current_player(), 'O')

if __name__ == '__main__':
    unittest.main()
