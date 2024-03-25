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
        words_line, *puzzle_lines = puzzle.split("\n")
        self.words: list[str] = words_line.split(",")
        self.puzzle: list[list[str]] = [line.split(",") for line in puzzle_lines]

        self.origin: Coordinate = Coordinate(0, 0)
        self.max_bounds: Coordinate = Coordinate(len(self.puzzle[0]), len(self.puzzle))

        self.directions: list[Coordinate] = [
            Coordinate(0, -1),
            Coordinate(1, 0),
            Coordinate(1, 1),
            Coordinate(-1, 1),
            Coordinate(-1, -1),
            Coordinate(-1, 0),
            Coordinate(0, 1),
            Coordinate(1, -1),
        ]
        self.word_trie_root: dict[str, dict] = WordSearch.make_trie(self.words)

    def search_for_words(self) -> dict[str, list[tuple[int, int]]]:
        results: dict[str, list[tuple[int, int]]] = {}
        for start in self.get_all_cell_coordinates():
            for direction in self.directions:
                for word, path in self.get_paths_and_words(start, direction):
                    results[word] = path
        return results

    def get_all_cell_coordinates(self) -> Iterable[Coordinate]:
        for x, y in product(range(self.max_bounds.x), range(self.max_bounds.y)):
            yield Coordinate(x, y)

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
        for cell in self.get_cell_coordinates_in_direction(start, direction):
            letter = self.get_cell_value(cell)
            yield cell, letter

    def get_cell_coordinates_in_direction(self, start, direction: Coordinate) -> Iterable[Coordinate]:
        current = start
        while self.is_coordinate_within_bounds(current):
            yield current
            current = current + direction

    def is_coordinate_within_bounds(self, coordinate: Coordinate) -> bool:
        return self.origin <= coordinate < self.max_bounds

    def get_cell_value(self, cell: Coordinate) -> str:
        return self.puzzle[cell.y][cell.x]

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
