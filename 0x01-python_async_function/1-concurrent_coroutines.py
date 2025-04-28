#!/usr/bin/env python3
"""Executing multiple coroutines at the same time."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats after waiting"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays: List[float] = []
    for delay in delays:
        # insert each delay into the sorted list in ascending order
        index = 0
        while index < len(sorted_delays) and sorted_delays[index] < delay:
            index += 1
        sorted_delays.insert(index, delay)

    return sorted_delays
