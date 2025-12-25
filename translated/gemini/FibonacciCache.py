import concurrent.futures

cache[0] = 0
cache[1] = 1

def fib(n):
    if n in cache:
        return cache[n]
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    cache.setdefault(n, b)
    return cache[n]

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    m = int(input())
    vals = list(map(int, input().split()))

    with concurrent.futures.ThreadPoolExecutor(max_workers=min(m, os.cpu_count())) as ex:
        futs = [ex.submit(fib, v) for v in vals]
        
        sb = []
        for fut in futs:
            sb.append(str(fut.result()))
        
        print(" ".join(sb))
import os