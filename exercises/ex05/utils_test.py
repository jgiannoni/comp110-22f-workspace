"""Utils test."""

__author__ = "730529967"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_evens() -> None:
    """Test only evens func. with all even numbers."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_only_evens_odds() -> None:
    """Test all even func. with all odd numbers."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_only_evens_mixed() -> None:
    """Test only even func with both even and odd numbers."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_concat_1() -> None:
    """First test concat with 2 lists."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    """Second test for concat with 2 lists."""
    list_1: list[int] = [7, 8, 9]
    list_2: list[int] = [1, 2, 3]
    assert concat(list_1, list_2) == [7, 8, 9, 1, 2, 3]


def test_concat_3() -> None:
    """Third test for concat with lists of different sizes."""
    list_1: list[int] = [1, 2]
    list_2: list[int] = [9, 4, 3]
    assert concat(list_1, list_2) == [1, 2, 9, 4, 3]


def test_sub_1() -> None:
    """First test for sub."""
    list_1: list[int] = [2, 3, 4, 5, 6]
    start: int = 2
    end: int = 4
    assert sub(list_1, start, end) == [4, 5]


def test_sub_2() -> None:
    """Second test for sub."""
    list_1: list[int] = [4, 2, 5, 8, 7, 1]
    start: int = 3
    end: int = 5
    assert sub(list_1, start, end) == [8, 7]


def test_sub_3() -> None:
    """Third test fr sub."""
    list_1: list[int] = [3, 4, 5, 2, 3, 2, 3]
    start: int = 4
    end: int = 6
    assert sub(list_1, start, end) == [3, 2]