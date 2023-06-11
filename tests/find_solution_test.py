import unittest
from hitori_logic.find_solution import (
    find_duplicates,
    paint_neighbors_horizontal_while,
    paint_single,
    paint_neighbors_white,
    paint_continuous_path,
    paint_in_lines_black,
    check_connected_white)


class HitoriLogicTests(unittest.TestCase):

    def test_find_duplicates(self):
        arr_board = [['1', '2', '3'],
                     ['1', '4', '5'],
                     ['1', '6', '1']]
        arr_col = [['g', 'g', 'g'],
                   ['g', 'g', 'g'],
                   ['g', 'g', 'g']]
        find_duplicates(arr_board, arr_col)
        expected_arr_col = [['b', 'g', 'g'],
                            ['w', 'g', 'g'],
                            ['b', 'g', 'g']]
        self.assertEqual(arr_col, expected_arr_col)

    def test_paint_neighbors_horizontal_while(self):
        i, j = 1, 1
        board_colors = [['g', 'g', 'g'],
                        ['g', 'b', 'g'],
                        ['g', 'g', 'g']]
        paint_neighbors_horizontal_while(i, j, board_colors)
        expected_board_colors = [['w', 'g', 'w'],
                                 ['g', 'b', 'g'],
                                 ['w', 'g', 'w']]
        self.assertEqual(board_colors, expected_board_colors)

    def test_paint_neighbors_white(self):
        board_colors = [['g', 'g', 'g'],
                        ['g', 'b', 'g'],
                        ['g', 'g', 'g']]
        paint_neighbors_white(board_colors)
        expected_board_colors = [['g', 'w', 'g'],
                                 ['w', 'b', 'w'],
                                 ['g', 'w', 'g']]
        self.assertEqual(board_colors, expected_board_colors)

    def test_paint_in_lines_black(self):
        board_colors = [['g', 'g', 'g'],
                        ['w', 'w', 'g'],
                        ['g', 'g', 'w']]
        board = [['1', '2', '3'],
                 ['1', '4', '5'],
                 ['1', '4', '1']]
        paint_in_lines_black(board_colors, board)
        expected_board_colors = [['b', 'g', 'g'],
                                 ['w', 'w', 'g'],
                                 ['b', 'b', 'w']]
        self.assertEqual(board_colors, expected_board_colors)

    def test_paint_single(self):
        board_colors = [['g', 'g', 'g'],
                        ['g', 'g', 'g'],
                        ['g', 'g', 'g']]
        board = [['1', '2', '3'],
                 ['1', '4', '5'],
                 ['1', '6', '1']]
        paint_single(board_colors, board)
        expected_board_colors = [['g', 'w', 'w'],
                                 ['g', 'w', 'w'],
                                 ['g', 'w', 'g']]
        self.assertEqual(board_colors, expected_board_colors)

    def test_paint_continuous_path(self):
        i, j = 1, 1
        board_colors = [['w', 'w', 'g'],
                        ['w', 'g', 'g'],
                        ['g', 'g', 'g']]
        paint_continuous_path(board_colors, i, j)
        expected_board_colors = [['w', 'w', 'g'],
                                 ['w', 'b', 'g'],
                                 ['g', 'g', 'g']]
        self.assertEqual(board_colors, expected_board_colors)

    def test_check_connected_white(self):
        array = [['w', 'w', 'g'],
                 ['g', 'w', 'g'],
                 ['g', 'w', 'g']]
        self.assertTrue(check_connected_white(array))
