from generator.generator import Generator
from generator.duplicate_strategy import DuplicateFiller
from generator.shade_map_strategy import RandomShader
from generator.initial_grid_populator import SwapPopulator

first_input_flag = True
columns = 0
generator = None


def change_flag():
    global first_input_flag
    first_input_flag = True


def input_size():
    input_flag = True
    while input_flag:
        try:
            size = int(input("Введите размер поля n x n от 6 до 10: "))
            if size < 6 or size > 10:
                continue
            input_flag = False
        except:
            continue

    return size


def make_generator(size):
    global generator, first_input_flag
    if size == 0:
        size = input_size()
    first_input_flag = False
    generator = Generator(size, SwapPopulator(), RandomShader(), DuplicateFiller())


def generate(size):
    global generator, first_input_flag
    if first_input_flag:
        make_generator(size)
    return generator.generate()


def input_board():
    input_flag = True
    board = []
    while input_flag:
        size = input("Введите размер поля n x n от 6 до 10: ")
        try:
            size_split = size.split('x')
            n = int(size_split[0])
            m = int(size_split[1])

        except:
            continue
        if (n or m) < 6 or (n or m) > 10:
            continue
        input_flag = False

    print('Введите поле:')
    input_flag = True
    while input_flag:
        for i in range(n):
            line = input()
            line_split = line.split()
            while len(line_split) != m:
                line = input(f'Введите {i + 1} строку верно: ')
                line_split = line.split()
            board.append(line_split)
        input_flag = False

    return board
