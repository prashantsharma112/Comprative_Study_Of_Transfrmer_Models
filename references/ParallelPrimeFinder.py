import sys
from concurrent.futures import ProcessPoolExecutor

parts = sys.stdin.read().strip().split()
start, end, chunks = int(parts[0]), int(parts[1]), int(parts[2])

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

def count_range(r):
    s,e = r
    cnt = 0
    for i in range(s,e+1):
        if is_prime(i): cnt += 1
    return cnt

rng = end - start + 1
chunk_size = max(1, rng // chunks)
ranges = []
s = start
while s <= end:
    e = min(end, s + chunk_size - 1)
    ranges.append((s,e))
    s = e + 1

with ProcessPoolExecutor() as ex:
    total = sum(ex.map(count_range, ranges))
print(total)
