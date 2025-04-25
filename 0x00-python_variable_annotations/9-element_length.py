#!/usr/bin/env python3
"""Function with proper type annotations"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with elements and their lengths"""
    return [(i, len(i)) for i in lst]
