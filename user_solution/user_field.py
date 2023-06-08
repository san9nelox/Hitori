from hitori_logic.find_solution import hitori_solution, return_board

board = None
board_colors = None


def generate_board(size):
    global board, board_colors
    hitori_solution(size)
    board = return_board()
    board_colors = [['g'] * len(board[0]) for _ in range(len(board))]


def return_user_board():
    return board


def return_user_board_colors():
    return board_colors
