from generator.generator import Generator
from generator.duplicate_strategy import DuplicateFiller
from generator.shade_map_strategy import RandomShader
from generator.initial_grid_populator import SwapPopulator

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

# generator = Generator(n, m, SwapPopulator(), RandomShader(), DuplicateFiller())
generator = Generator(n, n, SwapPopulator(), RandomShader(), DuplicateFiller())


# generator = Generator(6, 6, SwapPopulator(), RandomShader(), DuplicateFiller())


def generate():
    return generator.generate()
