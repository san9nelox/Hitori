import unittest
from hitori_logic.constant_converter import to_tuple, str_to_int, return_color


class MyModuleTests(unittest.TestCase):

    def test_to_tuple(self):
        self.assertEqual(to_tuple("(1, 2, 3)"), (1, 2, 3))
        self.assertEqual(to_tuple("(4, 5, 6)"), (4, 5, 6))
        self.assertEqual(to_tuple("(7, 8, 9)"), (7, 8, 9))

    def test_str_to_int(self):
        self.assertEqual(str_to_int(['1', '2', '3']), (1, 2, 3))
        self.assertEqual(str_to_int(['4', '5', '6']), (4, 5, 6))
        self.assertEqual(str_to_int(['7', '8', '9']), (7, 8, 9))

    def test_return_color(self):
        black, white, gray = return_color()
        self.assertEqual(black, (0, 0, 0))
        self.assertEqual(white, (255, 255, 255))
        self.assertEqual(gray, (128, 128, 128))


if __name__ == '__main__':
    unittest.main()
