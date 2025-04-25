#!/usr/bin/env python3
"""Validating zoom_array to ensure it passes mypy check"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """The function to be validated."""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
