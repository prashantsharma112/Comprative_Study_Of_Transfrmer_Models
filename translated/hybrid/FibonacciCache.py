import sys
import time
import math

def fib(n):
    if n in cache:
        return cache[n]
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    cache[n] = b
    return b

def main():
    sc = sys.stdin
    m = int(sc.readline())
    vals = []
    for _ in range(m):
        vals.append(int(sc.readline()))
    sc.close()

    ex = Executor(max_workers=min(m, os.cpu_count()))
    futs = []
    for v in vals:
        futs.append(ex.submit(fib, v))
    sb = ""
    for i in range(m):
        if i > 0: sb += " "
        sb += str(futs[i].result())
    ex.shutdown()
    print(sb)

if __name__ == "__main__":
    main()