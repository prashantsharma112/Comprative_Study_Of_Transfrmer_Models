import concurrent.futures
import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    import sys
    sc = sys.stdin
    start = int(sc.readline())
    end = int(sc.readline())
    chunks = int(sc.readline())

    range_size = end - start + 1
    chunk_size = max(1, range_size // chunks)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(chunks,  None)) as executor:
        futures = []
        s = start
        while s <= end:
            e = min(end, s + chunk_size - 1)
            
            futures.append(executor.submit(lambda ss, ee: sum(1 for i in range(ss, ee + 1) if is_prime(i)), s, e))
            s = e + 1
            
        total = sum(f.result() for f in futures)

    print(total)