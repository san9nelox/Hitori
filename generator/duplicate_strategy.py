from abc import ABC, abstractmethod
import random
from typing import List


class DuplicateStrategy(ABC):
    @abstractmethod
    def fill(self, base: List[int], shade_map: List[bool], size: int, random: random.Random) -> None:
        pass


class DuplicateFiller(DuplicateStrategy):
    def __init__(self):
        self.random = None
        self.size = None
        self.data = None
        self.shade_map = None
        self.max_size = None

    def fill(self, base, shade_map, size, random):
        self.data = base
        self.shade_map = shade_map
        self.size = size
        self.random = random

        self.apply_duplicates()

    def apply_duplicates(self):

        # Take the shaded cells and determine numbers that are duplicate to others
        # in the row or col
        for r in range(self.size):
            for c in range(self.size):
                if not self.shade_map[r * self.size + c]:
                    continue

                # This is a shaded cell
                # Find a number that will work here

                # Maybe we can use a mask
                # each bit is a number
                # 1 means we can use that number, 0 not
                # generate a mask for the row and the col
                # or them together
                # any of those numbers should be ok

                mask = self.gen_row_mask(r, self.shade_map) | self.gen_col_mask(c, self.shade_map)
                if mask == 0:
                    continue
                value = self.random_number(mask)
                self.data[r][c] = value

    def gen_row_mask(self, r, shade_map):
        mask = 0
        for c in range(self.size):
            # As long as it is not shaded
            if not shade_map[r * self.size + c]:
                # Can use the number
                mask |= (1 << self.data[r][c])

        return mask

    def gen_col_mask(self, c, shade_map):
        mask = 0
        for r in range(self.size):
            # As long as it is not shaded
            if not shade_map[r * self.size + c]:
                # Can use the number
                mask |= (1 << self.data[r][c])

        return mask

    def random_number(self, mask):
        # Work out how many we can choose from
        choices = 0
        for i in range(1, self.size + 1):
            if mask & (1 << i) != 0:
                choices += 1

        choice = random.randint(0, choices - 1)

        # Find the value
        for i in range(1, self.size + 1):
            if mask & (1 << i) != 0:
                if choice == 0:
                    return i
                else:
                    choice -= 1

        raise AssertionError("Cannot reach here")
