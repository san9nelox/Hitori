import unittest
from user_solution.check_solution import *
from hitori_logic.find_solution import set_final_board


class HitoriLogicTests(unittest.TestCase):

    def test_check_no_gray_with_gray(self):
        board_colors = [
            ['g', 'b', 'w'],
            ['w', 'g', 'b'],
            ['b', 'w', 'g']
        ]
        result = check_no_gray(board_colors)
        self.assertFalse(result)

    def test_check_no_gray_without_gray(self):
        board_colors = [
            ['b', 'b', 'w'],
            ['w', 'b', 'b'],
            ['b', 'w', 'w']
        ]
        result = check_no_gray(board_colors)
        self.assertTrue(result)

    def test_check_black_neigh_with_black_neighbors(self):
        board_colors = [
            ['w', 'b', 'w'],
            ['b', 'w', 'b'],
            ['w', 'b', 'w']
        ]
        result = check_black_neigh(board_colors)
        self.assertTrue(result)

    def test_check_black_neigh_with_black_neighbors(self):
        board_colors = [
            ['w', 'b', 'w'],
            ['w', 'b', 'b'],
            ['w', 'b', 'w']
        ]
        result = check_black_neigh(board_colors)
        self.assertFalse(result)

    def test_check_duplicates_in_row_with_duplicates(self):
        board_colors = [
            ['w', 'w', 'w'],
            ['w', 'w', 'w'],
            ['w', 'w', 'w']
        ]
        result = check_duplicates_in_row(board_colors)
        self.assertFalse(result)

    def test_check_duplicates_in_column_without_duplicates(self):
        board_colors = [
            ['w', 'b', 'w'],
            ['w', 'w', 'b'],
            ['b', 'w', 'w']
        ]
        result = check_duplicates_in_column(board_colors)
        self.assertTrue(result)

    def test_all_check_with_no_exceptions(self):
        set_final_board([
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ])
        board_colors = [
            ['w', 'b', 'w'],
            ['w', 'w', 'w'],
            ['w', 'b', 'w']
        ]
        result = all_check(board_colors)
        self.assertEqual('win', result)

    def test_all_check_with_gray_exception(self):
        board_colors = [
            ['g', 'b', 'w'],
            ['b', 'w', 'b'],
            ['w', 'b', 'w']
        ]
        result = all_check(board_colors)
        self.assertEqual('gray exception', result)

    def test_all_check_with_black_exception(self):
        board_colors = [
            ['w', 'b', 'b'],
            ['b', 'w', 'b'],
            ['w', 'b', 'w']
        ]
        result = all_check(board_colors)
        self.assertEqual('black exception', result)

    def test_all_check_with_row_exception(self):
        set_final_board([
            ['1', '2', '1'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ])
        board_colors = [
            ['w', 'b', 'w'],
            ['b', 'w', 'b'],
            ['w', 'w', 'w']
        ]
        result = all_check(board_colors)
        self.assertEqual('row exception', result)

    def test_all_check_with_column_exception(self):
        set_final_board([
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '3']
        ])
        board_colors = [
            ['w', 'b', 'w'],
            ['b', 'w', 'b'],
            ['w', 'w', 'w']
        ]
        result = all_check(board_colors)
        self.assertEqual('column exception', result)

    def test_all_check_with_neigh_exception(self):
        set_final_board([
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '5']
        ])
        board_colors = [
            ['w', 'w', 'w'],
            ['b', 'w', 'b'],
            ['w', 'w', 'w']
        ]
        result = all_check(board_colors)
        self.assertEqual('neigh exception', result)


if __name__ == '__main__':
    unittest.main()
