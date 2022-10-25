"""Dictionary exercise 7."""

__author__ = "730529967"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert function."""
    d: dict[str, str] = {}
    key: str = ""
    for key in x:
        if x[key] in d:
            raise KeyError("Key Error.")
        else:
            d[x[key]] = key
    return (d)


def favorite_color(x: dict[str, str]) -> str:
    """Favorite color function."""
    i: int = 0 
    s: str = ""
    d: dict[str, int] = {}
    for key in x:
        if x[key] in d:
            d[x[key]] += 1
        else:
            d[x[key]] = 1
    for key in d:
        if d[key] > i:
            i = d[key]
            s = key
        else:
            s = s
    return s


def count(x: list[str]) -> dict[str, int]:
    """Count function."""
    d: dict[str, int] = {}
    i: int = 0 
    for x[i] in x:
        if x[i] in d:
            d[x[i]] += 1
            i += 1
        else:
            d[x[i]] = 1
            i += 1
    return d
