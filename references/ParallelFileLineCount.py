import sys
from concurrent.futures import ThreadPoolExecutor

n = int(sys.stdin.readline().strip())
files = [sys.stdin.readline().strip() for _ in range(n)]

def count_lines(fn):
    c = 0
    try:
        with open(fn, 'r') as f:
            for _ in f:
                c += 1
    except:
        pass
    return c

with ThreadPoolExecutor(max_workers=min(n, 8)) as ex:
    total = sum(ex.map(count_lines, files))
print(total)
