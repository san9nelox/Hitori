from generator.duplicate_strategy import DuplicateStrategy
from generator.shade_map_strategy import ShadeMapStrategy
from generator.initial_grid_populator import InitialGridPopulator
import random


class Generator:
    def __init__(self, size_row: int, size_col, initial_populator: InitialGridPopulator,
                 shade_strategy: ShadeMapStrategy,
                 duplicate_strategy: DuplicateStrategy, random_seed: int = None):
        self.size_row = size_row
        self.size_col = size_col
        self.initial_populator = initial_populator
        self.shade_strategy = shade_strategy
        self.duplicate_strategy = duplicate_strategy

        if random_seed is None:
            random_seed = random.randint(0, 2 ** 32 - 1)
        print(f"Seed: {random_seed}")
        self.random = random.Random(random_seed)
        self.data = [[0] * self.size_col for _ in range(self.size_row)]

    def generate(self):
        self.initial_populator.populate(self.data, self.size_row, self.size_col, self.random)
        shade_map = [False] * (self.size_row * self.size_col)
        self.shade_strategy.generate(shade_map, self.size_row, self.size_col, self.random)
        self.duplicate_strategy.fill(self.data, shade_map, self.size_row, self.size_col, self.random)

        return self.data
