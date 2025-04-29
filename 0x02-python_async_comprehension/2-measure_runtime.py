#!/usr/bin/env python3
"""Calculating run time for four parallel comprehensions"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure run time of four parrallel coroutines."""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start
