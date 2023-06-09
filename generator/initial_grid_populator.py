from abc import ABC, abstractmethod
import random
from typing import List


class InitialGridPopulator(ABC):
    @abstractmethod
    def populate(self, data: List[int], size: int, random: random.Random) -> None:
        pass


class SwapPopulator(InitialGridPopulator):
    def populate(self, data, size, random):
        # Initial grid
        for r in range(size):
            for c in range(size):
                data[r][c] = (c + r) % size + 1

        # Swap columns and rows for a while
        count = 10
        for c in range(count):
            # Select 2 columns
            from_col = random.randint(0, size - 1)
            to_col = random.randint(0, size - 2)
            if to_col >= from_col:
                to_col += 1

            # Swap them
            for i in range(size):
                temp = data[i][to_col]
                data[i][to_col] = data[i][from_col]
                data[i][from_col] = temp

            # Select 2 rows
            from_row = random.randint(0, size - 1)
            to_row = random.randint(0, size - 2)
            if to_row >= from_row:
                to_row += 1

            # Swap them
            for i in range(size):
                temp = data[to_row][i]
                data[to_row][i] = data[from_row][i]
                data[from_row][i] = temp
