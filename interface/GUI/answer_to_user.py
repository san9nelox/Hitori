from user_solution.check_solution import all_check


def check_win(board_colors):
    answer = all_check(board_colors)
    match answer:
        case 'gray exception':
            return 'Не все клетки закрашены'
        case 'black exception':
            return 'Есть черные соседи'
        case 'row exception':
            return 'В строке есть одинаковые цифры'
        case 'column exception':
            return 'В столбце есть одинаковые цифры'
        case 'neigh exception':
            return 'Есть одинаковые соседи'
        case 'connection exception':
            return 'Не все белые соединены'
        case 'win':
            return 'С победой'
