#!/usr/bin/env python3
"""Takes a mixed list of integers and float return a floating point sum."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns an sum of floats and intergers"""
    return sum(mxd_lst)
