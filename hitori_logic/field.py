from generator.generator import Generator
from generator.duplicate_strategy import DuplicateFiller
from generator.shade_map_strategy import RandomShader
from generator.initial_grid_populator import SwapPopulator

first_input_flag = True
rows = 0
columns = 0
generator = None


def change_flag():
    global first_input_flag
    first_input_flag = True


def input_size():
    global first_input_flag
    input_flag = True
    while input_flag:
        size = input("Введите размер поля n x n от 6 до 10: ")
        try:
            size_split = size.split('x')
            n = int(size_split[0])
            # m = int(size_split[1])
            if n < 6 or n > 10:
                continue
            input_flag = False
        except:
            continue
    first_input_flag = False

    return n


def make_generator():
    global rows, generator
    rows = input_size()
    generator = Generator(rows, rows, SwapPopulator(), RandomShader(), DuplicateFiller())
    # generator = Generator(rows, columns, SwapPopulator(), RandomShader(), DuplicateFiller())
    # generator = Generator(6, 6, SwapPopulator(), RandomShader(), DuplicateFiller())


def generate():
    global generator, first_input_flag
    if first_input_flag:
        make_generator()
    return generator.generate()


def input_board():
    input_flag = True
    board = []
    while input_flag:
        try:
            size = int(input("Введите размер поля n x n от 6 до 10: "))
        except ValueError:
            continue
        if size < 6 or size > 10:
            continue
        input_flag = False

    print('Введите поле:')
    input_flag = True
    while input_flag:
        for i in range(size):
            line = input()
            line_split = line.split()
            while len(line_split) != size:
                line = input(f'Введите {i + 1} строку верно: ')
                line_split = line.split()
            board.append(line_split)
        input_flag = False

    return board
