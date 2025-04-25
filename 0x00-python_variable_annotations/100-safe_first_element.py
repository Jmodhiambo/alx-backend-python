#!/usr/bin/env python3
"""Duck-typed annotation for safe_first_element"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element if it exists, else None"""
    if lst:
        return lst[0]
    else:
        return None
