"""EX04 utils."""
__author__ = "730529967"


def all(list_int: list[int], single_int: int) -> bool:
    """Check if single integer matches all in list."""
    i: int = 0
    while i < int(len(list_int)):
        if list_int[i] != single_int:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Max."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    store: int = input[0]
    while i < len(input):
        if input[i] > store:
            store = input[i]
            i = i + 1
        else:
            i = i + 1
    return store


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Is equal."""
    i: int = 0 
    while i < len(list1):
        if list1[i] == list2[i]:
            i +=1
        else:
            return False
    return True
