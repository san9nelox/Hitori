import random


def generate_board(size):
    board = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = random.randint(1, size)
    return board


def print_board(board):
    for row in board:
        print(row)


size = int(input("Введите размер поля от 6 до 12: "))
if size < 6 or size > 12:
    while size < 6 or size > 12:
        size = int(input("Введите размер поля от 6 до 12: "))

board = generate_board(size)
print("Сгенерированное поле:")
print_board(board)
