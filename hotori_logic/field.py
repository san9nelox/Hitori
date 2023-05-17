import random


def generate_board(rows, columns):
    rectangle = [[0 for j in range(columns)] for i in range(rows)]

    for i in range(rows):
        for j in range(columns):
            rectangle[i][j] = random.randint(1, 9)
    return rectangle


def print_board(rectangle):
    for i in range(n):
        for j in range(m):
            print(rectangle[i][j], end=' ')
        print()


input_flag = True
while input_flag:
    size = input("Введите размер поля n x m от 6 до 10: ")
    try:
        size_split = size.split('x')
        n = int(size_split[0])
        m = int(size_split[1])
        if n < 6 or n > 10 or m < 6 or m > 10:
            continue
        input_flag = False
    except:
        continue

board = generate_board(n, m)
