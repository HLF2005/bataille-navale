
from typing import Iterable, Tuple

Coord = Tuple[int, int]

def overlaps(a: Iterable[Coord], b: Iterable[Coord]) -> bool:
    sa, sb = set(a), set(b)
    return len(sa & sb) > 0