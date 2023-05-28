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
    first_input_flag = False

    return n, m


def make_generator():
    global rows, columns, generator
    rows, columns = input_size()
    generator = Generator(rows, rows, SwapPopulator(), RandomShader(), DuplicateFiller())
    # generator = Generator(n, m, SwapPopulator(), RandomShader(), DuplicateFiller())
    # generator = Generator(6, 6, SwapPopulator(), RandomShader(), DuplicateFiller())


def generate():
    global generator, first_input_flag
    if first_input_flag:
        make_generator()
    return generator.generate()
