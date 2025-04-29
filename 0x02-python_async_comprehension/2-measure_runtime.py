#!/usr/bin/env python3
"""Calculating run time for four parallel comprehensions"""

import time
import asyncio

ac = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure run time of four parrallel coroutines."""
    start = time.perf_counter()
    await asyncio.gather(ac(), ac(), ac(), ac())
    return time.perf_counter() - start
