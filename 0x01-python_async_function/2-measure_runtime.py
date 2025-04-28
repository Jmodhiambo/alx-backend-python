#!/usr/bin/env python3
"""Measuring runtime"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the time taken by the wait_n function"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))

    return (time.perf_counter() - start) / n
