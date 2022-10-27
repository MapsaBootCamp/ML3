from typing import Dict


### DP: optimization   

def fibo(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def fibo_optimize(n: int, cache = {1: 1, 2: 1}) ->  int:
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibo_optimize(n-1) + fibo_optimize(n-2)
        return cache[n]


def fibo_bu(n: int) -> int:
    first, second = 1, 1
    for i in range(n - 1):
        first, second = second, first + second
    return first



# print((fibo_optimize(500)))
print(fibo_bu(3))


