from hitori_logic.find_solution import check_connected_white
from user_solution.user_field import board


def check_no_gray(board_colors):
    for i in range(len(board_colors)):
        for j in range(len(board_colors[i])):
            if board_colors[i][j] == 'g':
                return False
    return True


def check_duplicates_in_row(board_colors):
    for i in range(len(board_colors)):
        for j in range(len(board_colors[i])):
            if board_colors[i][j] == 'w':
                for k in range(j, len(board_colors[i])):
                    if k != j and board[i][j] == board[i][k] and board_colors[i][k] == 'w':
                        return False
    return True


def check_duplicates_in_column(board_colors):
    for i in range(len(board_colors)):
        for j in range(len(board_colors[i])):
            if board_colors[i][j] == 'w':
                for k in range(i, len(board_colors)):
                    if k != i and board[i][j] == board[k][j] and board_colors[k][j] == 'w':
                        return False
    return True


def check_horizontal_neigh(board_colors):
    for i in range(len(board_colors)):
        for j in range(len(board_colors[i])):
            if board_colors[i][j] == 'w':
                if i > 0:
                    if board_colors[i - 1][j] == 'w' and board[i][j] == board[i - 1][j]:
                        return False
                if i < len(board_colors) - 1:
                    if board_colors[i + 1][j] == 'w' and board[i][j] == board[i + 1][j]:
                        return False
                if j > 0:
                    if board_colors[i][j - 1] == 'w' and board[i][j] == board[i][j - 1]:
                        return False
                if j < len(board_colors[i]) - 1:
                    if board_colors[i][j + 1] == 'w' and board[i][j] == board[i][j + 1]:
                        return False
    return True


def all_check(board_colors):
    if not check_no_gray(board_colors):
        return 'gray exeption'
    if not check_duplicates_in_row(board_colors):
        return 'row exeption'
    if not check_duplicates_in_column(board_colors):
        return 'column exeption'
    if not check_horizontal_neigh(board_colors):
        return 'neigh exeption'
    if not check_connected_white(board_colors):
        return 'connection exeption'
    return 'win'
