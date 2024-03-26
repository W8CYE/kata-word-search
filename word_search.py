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
        self.words, *self.puzzle = [line.split(",") for line in puzzle.split("\n")]
        self.dimension = len(self.puzzle)
        self.word_trie_root: dict[str, dict] = WordSearch.make_trie(self.words)

    def search_for_words(self) -> dict[str, list[tuple[int, int]]]:
        cells = (Coordinate(x, y) for x, y in product(range(self.dimension), repeat=2))
        directions = (Coordinate(dx, dy) for dx, dy in product([-1, 0, 1], repeat=2) if (dx, dy) != (0, 0))

        # does not account for multiple instances of the same word in a puzzle
        results: dict[str, list[tuple[int, int]]] = {}

        for start, direction in product(cells, directions):
            for word, path in self.get_paths_and_words(start, direction):
                results[word] = path
        return results

    def get_paths_and_words(self, start: Coordinate, direction: Coordinate) -> Iterable[tuple[str, list[tuple[int, int]]]]:
        path: list[tuple[int, int]] = []
        letters: list[str] = []
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
        while Coordinate(0, 0) <= current < Coordinate(self.dimension, self.dimension):
            yield current, self.puzzle[current.y][current.x]
            current = current + direction

    @staticmethod
    def make_trie(words: list[str]) -> dict[str, dict]:
        root: dict[str, dict] = {}
        for word in words:
            node = root
            for letter in word:
                node = node.setdefault(letter, {})
            node["END"] = {}
        return root


# NOODLES BEYOND THIS POINT


def get_english_words(length: int = 3) -> list[str]:
    # path to dictionary on macos
    with open("/usr/share/dict/words", "r", encoding="utf-8") as f:
        words = f.read().splitlines()
    res = [word.upper() for word in words if len(word) >= length]
    print(f"searching with {len(res):,} dictionary words of at least {length} letters")
    return res


if __name__ == "__main__":
    with open("input2.txt", "r", encoding="utf-8") as file:
        puzzle_from_file = file.read()
    word_search = WordSearch(puzzle_from_file)
    # user full dictionary words instead of seed words
    # word_search.word_trie_root = WordSearch.make_trie(get_english_words(5))

    for word, path in word_search.search_for_words().items():
        print(word, path)
