from generator.duplicate_strategy import DuplicateStrategy
from generator.shade_map_strategy import ShadeMapStrategy
from generator.initial_grid_populator import InitialGridPopulator
import random


class Generator:
    def __init__(self, size_row: int, initial_populator: InitialGridPopulator,
                 shade_strategy: ShadeMapStrategy,
                 duplicate_strategy: DuplicateStrategy, random_seed: int = None):
        self.size = size_row
        self.initial_populator = initial_populator
        self.shade_strategy = shade_strategy
        self.duplicate_strategy = duplicate_strategy

        if random_seed is None:
            random_seed = random.randint(0, 2 ** 32 - 1)
        self.random = random.Random(random_seed)
        self.data = [[0] * self.size for _ in range(self.size)]

    def generate(self):
        self.initial_populator.populate(self.data, self.size, self.random)
        shade_map = [False] * (self.size * self.size)
        self.shade_strategy.generate(shade_map, self.size, self.random)
        self.duplicate_strategy.fill(self.data, shade_map, self.size, self.random)

        return self.data
