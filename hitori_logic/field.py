import random


def generate_board(rows, columns, min_size):
    rectangle = [[0 for j in range(columns)] for i in range(rows)]

    for i in range(rows):
        for j in range(columns):
            rectangle[i][j] = random.randint(1, min_size)
    return check_and_replace(rectangle, min_size)


def check_and_replace(arr, n):
    # Проверяем строки
    for i in range(len(arr)):
        count = 1
        for j in range(1, len(arr[i])):
            if arr[i][j] == arr[i][j - 1]:
                count += 1
                if count >= 4:
                    arr[i][j] = random.randint(0, n)
                    count = 1
            else:
                count = 1

    # Проверяем столбцы
    for j in range(len(arr[0])):
        count = 1
        for i in range(1, len(arr)):
            if arr[i][j] == arr[i - 1][j]:
                count += 1
                if count >= 4:
                    arr[i][j] = random.randint(0, n)
                    count = 1
            else:
                count = 1

    return arr


def print_board(rectangle, rows, colums):
    for i in range(rows):
        for j in range(colums):
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

min_size = min(n, m)
board = generate_board(n, m, min_size)
print_board(board, n, m)
