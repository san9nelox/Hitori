import pygame
from hitori_logic.constant_converter import return_color
from user_solution.check_solution import all_check


def check_win(board_colors):
    answer = all_check(board_colors)
    match answer:
        case 'gray exeption':
            return 'Не все клетки закрашены'
        case 'row exeption':
            return 'В строке есть одинаковые цифры'
        case 'column exeption':
            return 'В столбце есть одинаковые цифры'
        case 'neigh exeption':
            return 'Есть одинаковые соседи'
        case 'connection exeption':
            return 'Не белые соединены'
        case 'win':
            return 'С победой'
