#!/usr/bin/env python3
"""Takes a string and integer or float and return a tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes in a string and int or float and returns a tuple."""
    return (k, v ** 2)
