# pylint: disable=missing-docstring

from itertools import product
from dataclasses import dataclass
from typing import Iterable


@dataclass
class Coordinate:
    x: int
    y: int

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"({self.x:2}, {self.y:2})"

    def to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)


class WordSearch:
    def __init__(self, puzzle: str) -> None:
        self.words, self.puzzle = self._parse_puzzle(puzzle)
        self.origin: Coordinate = Coordinate(0, 0)
        self.max_bounds: Coordinate = Coordinate(len(self.puzzle[0]), len(self.puzzle))
        self.directions = [Coordinate(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)]
        self.word_trie_root: dict[str, dict] = WordSearch._make_trie(self.words)

    def _parse_puzzle(self, puzzle: str) -> tuple[list[str], list[list[str]]]:
        words_line, *puzzle_lines = puzzle.split("\n")
        words = words_line.split(",")
        puzzled = [line.split(",") for line in puzzle_lines]
        return words, puzzled

    def search_for_words(self) -> dict[str, list[tuple[int, int]]]:
        # does not account for multiple instances of the same word
        results: dict[str, list[tuple[int, int]]] = {}
        for x, y in product(range(self.max_bounds.x), range(self.max_bounds.y)):
            for direction in self.directions:
                for word, path in self.get_paths_and_words(Coordinate(x, y), direction):
                    results[word] = path
        return results

    def get_paths_and_words(self, start: Coordinate, direction: Coordinate) -> Iterable[tuple[str, list[tuple[int, int]]]]:
        path: list[tuple[int, int]] = []
        letters: list[str] = []  # [str(direction), " : "]
        words_node: dict[str, dict] = self.word_trie_root

        for cell, letter in self.get_cell_coordinates_and_values(start, direction):
            if letter not in words_node:
                return
            letters.append(letter)
            path.append(cell.to_tuple())
            words_node = words_node[letter]
            if "END" in words_node:
                yield "".join(letters), path

    def get_cell_coordinates_and_values(self, start: Coordinate, direction: Coordinate) -> Iterable[tuple[Coordinate, str]]:
        current = start
        while self.origin <= current < self.max_bounds:
            yield current, self.get_cell_value(current)
            current = current + direction

    def get_cell_value(self, cell: Coordinate) -> str:
        return self.puzzle[cell.y][cell.x]

    @staticmethod
    def _make_trie(words: list[str]) -> dict[str, dict]:
        root: dict[str, dict] = {}
        for word in words:
            node = root
            for letter in word:
                node = node.setdefault(letter, {})
            node["END"] = {}
        return root


# NOODLES BEYOND THIS POINT


# def get_english_words(length: int = 3) -> list[str]:
#     # path to dictionary on macos
#     with open("/usr/share/dict/words", "r", encoding="utf-8") as f:
#         words = f.read().splitlines()
#     res = [word.upper() for word in words if len(word) >= length]
#     print(f"searching with {len(res):,} dictionary words of at least {length} letters")
#     return res


# if __name__ == "__main__":
#     with open("input2.txt", "r", encoding="utf-8") as file:
#         puzzle_from_file = file.read()
#     word_search = WordSearch(puzzle_from_file)
#     # user full dictionary words instead of seed words
#     # word_search.word_trie_root = WordSearch.make_trie(get_english_words(5))

#     for word, path in word_search.search_for_words().items():
#         print(word, path)
