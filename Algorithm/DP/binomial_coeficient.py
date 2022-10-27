import time
from typing import Dict, Tuple


def bc(n: int, k: int, cache: Dict[Tuple, int] = {}) -> int:
    if n == k or k == 0:
        return 1
    if (n , k) in cache:
        return cache[(n, k)]
    else:
        cache[(n, k)] =  bc(n - 1, k) + bc(n - 1, k - 1)
        return cache[(n, k)]

old_time = time.time()
print(bc(500, 200))
print(time.time() - old_time)