import sys
from concurrent.futures import ThreadPoolExecutor

parts = sys.stdin.read().strip().split()
m = int(parts[0])
vals = [int(x) for x in parts[1:1+m]]

cache = {0:0, 1:1}
cache_lock = __import__('threading').Lock()

def fib(n):
    with cache_lock:
        if n in cache:
            return cache[n]
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    with cache_lock:
        cache.setdefault(n, b)
        return cache[n]

with ThreadPoolExecutor(max_workers=min(m, 8)) as ex:
    res = list(ex.map(fib, vals))
print(" ".join(str(x) for x in res))
