"""Dictionary exercise 7."""

__author__ = "730529967"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def count_test_1() -> None:
    """Count Test 1."""
    x: list[str] = {"r", "r", "b", "g"}
    assert count(x) == {}


def count_test_2() -> None:
    """Count Test 2."""
    x: list[str] = {}
    assert count(x) == {}


def count_test_3() -> None:
    """Count Test 3."""
    x: list[str] = {"r", "r", "b", "g"}
    assert count(x) == {}


def favorite_color_test_1() -> None:
    """Favorite Color Test 1."""
    x: dict[str, str] = {}
    assert favorite_color(x) == ""


def favorite_color_test_2() -> None:
    """Favorite Color Test 2."""
    x: dict[str, str] = {"Paul": "blue", "Brit": "red", "Aiden": "red"}
    assert favorite_color(x) == "red"


def favorite_color_test_3() -> None:
    """Favorite Color Test 3."""
    x: dict[str, str] = {"Paul": "blue", "Jared": "red", "Ashley": "blue"}
    assert favorite_color(x) == "blue"


def invert_test_1() -> None:
    """Invert Test 1."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def invert_test_2() -> None:
    """Invert Test 2."""
    x: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(x) == "'z': 'a', 'y': 'b', 'x': 'c'"


def invert_test_3() -> None:
    """Invert Test 3."""
    x: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(x) == "KeyError: 'Key Error.'"