"""Utils."""

__author__ = "730529967"


def only_evens(xs: list[int]) -> int:
    """Returns only even numbers."""
    i: int = 0 
    evens: list[int] = ([])
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
            i += 1
        else:
            i += 1
    return (evens) 


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Concatenate lists of ints."""
    new_list: list[int] = list_1 + list_2
    return (new_list)


def sub(list_1: list[int], start: int, end: int) -> list[int]:
    """Shows part of list between numbers."""
    new_list = list_1[start:end]
    return (new_list) 

   
        
