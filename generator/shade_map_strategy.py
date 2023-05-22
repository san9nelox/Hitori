import collections
from abc import ABC, abstractmethod
from typing import List
import numpy as np
import random


class ShadeMapStrategy(ABC):
    @abstractmethod
    def generate(self, shade_map: List[bool], size_row: int, size_col: int, random: random.Random) -> None:
        pass


class RandomShader(ShadeMapStrategy):
    def __init__(self, frequency=-1):
        # if frequency <= 0:
        #     raise ValueError("Invalid frequency")
        self.frequency = frequency
        self.isFrequencyFixed = True if frequency > 0 else False
        self.shadeMap = None
        self.size_row = 0
        self.size_col = 0
        self.random = None

    def generate(self, shade_map, size_row, size_col, random):
        if not self.isFrequencyFixed:
            self.frequency = (size_row * size_col) // 2

        self.shadeMap = shade_map
        self.size_row = size_row
        self.size_col = size_col
        self.random = random

        self.random_shade()
        self.make_continuous()
        self.fill_empty()

    def random_shade(self):
        added = 0
        while added < self.frequency:
            index = random.randint(0, len(self.shadeMap) - 1)

            ok = True
            next_index = self.index(index, 0, -1)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            next_index = self.index(index, 0, 1)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            next_index = self.index(index, 1, 0)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            next_index = self.index(index, -1, 0)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            if ok:
                self.shadeMap[index] = True
                added += 1

    def make_continuous(self):
        visited = np.copy(self.shadeMap)

        can_reach_all = False
        search = [1]
        while not can_reach_all and len(search) > 0:
            search = []
            for i in range(len(self.shadeMap)):
                if visited[i]:
                    continue
                search.append(i)
                break

            while search:
                index = search.pop()
                visited[index] = True

                next_index = self.index(index, 0, -1)
                if next_index >= 0 and not visited[next_index] and not self.shadeMap[next_index]:
                    search.append(next_index)

                next_index = self.index(index, 0, 1)
                if next_index >= 0 and not visited[next_index] and not self.shadeMap[next_index]:
                    search.append(next_index)

                next_index = self.index(index, -1, 0)
                if next_index >= 0 and not visited[next_index] and not self.shadeMap[next_index]:
                    search.append(next_index)

                next_index = self.index(index, 1, 0)
                if next_index >= 0 and not visited[next_index] and not self.shadeMap[next_index]:
                    search.append(next_index)

            can_reach_all = True
            for i in range(len(visited)):
                if not visited[i]:
                    can_reach_all = False
                    done = False
                    next_index = self.index(i, -1, -1)
                    if next_index >= 0 and visited[next_index] and not self.shadeMap[next_index]:
                        self.remove_shaded(i, -1, -1)
                        done = True

                    next_index = self.index(i, -1, 1)
                    if next_index >= 0 and visited[next_index] and not self.shadeMap[next_index]:
                        self.remove_shaded(i, -1, 1)
                        done = True

                    next_index = self.index(i, 1, -1)
                    if next_index >= 0 and visited[next_index] and not self.shadeMap[next_index]:
                        self.remove_shaded(i, 1, -1)
                        done = True

                    next_index = self.index(i, 1, 1)
                    if next_index >= 0 and visited[next_index] and not self.shadeMap[next_index]:
                        self.remove_shaded(i, 1, 1)
                        done = True

                    if done:
                        break

            visited = np.copy(self.shadeMap)

    def fill_empty(self):
        potentials = []
        for i in range(len(self.shadeMap)):
            if self.shadeMap[i]:
                continue

            next_index = self.index(i, 0, -1)
            if next_index >= 0 and self.shadeMap[next_index]:
                continue

            next_index = self.index(i, 0, 1)
            if next_index >= 0 and self.shadeMap[next_index]:
                continue

            next_index = self.index(i, -1, 0)
            if next_index >= 0 and self.shadeMap[next_index]:
                continue

            next_index = self.index(i, 1, 0)
            if next_index >= 0 and self.shadeMap[next_index]:
                continue

            potentials.append(i)

        while potentials:
            array_index = random.randint(0, len(potentials) - 1)
            index = potentials.pop(array_index)

            ok = True
            next_index = self.index(index, 0, -1)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            next_index = self.index(index, 0, 1)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            next_index = self.index(index, -1, 0)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            next_index = self.index(index, 1, 0)
            if next_index >= 0 and self.shadeMap[next_index]:
                ok = False

            if not ok:
                continue

            if self.can_reach_neighbours(self.shadeMap, index):
                self.shadeMap[index] = True

    def index(self, start, dr, dc):
        r = start // self.size_row
        c = start // self.size_col

        r += dr
        c += dc

        if r < 0 or r >= self.size_row:
            return -1
        if c < 0 or c >= self.size_col:
            return -1

        return c + r * self.size_row

    def remove_shaded(self, root, dr, dc):
        r = root // self.size_row
        c = root % self.size_col

        r += dr
        c += dc

        is_horizontal = random.choice([True, False])

        if r < 0 or r >= self.size_row:
            # Can't do vertical
            is_horizontal = True
        elif c < 0 or c >= self.size_col:
            # Can't do horizontal
            is_horizontal = False

        if is_horizontal:
            # Horizontal
            self.shadeMap[self.index(root, 0, dc)] = False
        else:
            # Vertical
            self.shadeMap[self.index(root, dr, 0)] = False

    def can_reach_neighbours(self, shade_map, start):
        visited = shade_map.copy()

        visited[start] = True

        # Neighbour indices
        left = self.index(start, 0, -1)
        right = self.index(start, 0, 1)
        up = self.index(start, -1, 0)
        down = self.index(start, 1, 0)

        search = collections.deque()
        if left >= 0:
            search.append(left)
        elif right >= 0:
            search.append(right)
        elif up >= 0:
            search.append(up)
        elif down >= 0:
            search.append(down)

        # Flood
        while search:
            index = search.pop()
            visited[index] = True

            # Left
            next_index = self.index(index, 0, -1)
            if next_index >= 0 and not visited[next_index] and not shade_map[next_index]:
                search.append(next_index)

            # Right
            next_index = self.index(index, 0, 1)
            if next_index >= 0 and not visited[next_index] and not shade_map[next_index]:
                search.append(next_index)

            # Up
            next_index = self.index(index, -1, 0)
            if next_index >= 0 and not visited[next_index] and not shade_map[next_index]:
                search.append(next_index)

            # Down
            next_index = self.index(index, 1, 0)
            if next_index >= 0 and not visited[next_index] and not shade_map[next_index]:
                search.append(next_index)

        # Check all are visited
        if left >= 0 and not visited[left]:
            return False

        if right >= 0 and not visited[right]:
            return False

        if up >= 0 and not visited[up]:
            return False

        if down >= 0 and not visited[down]:
            return False

        return True
