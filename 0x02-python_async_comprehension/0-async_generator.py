#!/usr/bin/env python3
"""Async generator"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield a random float between 0 and 10 asynchronously,
    10 times with a 1-second delay each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
