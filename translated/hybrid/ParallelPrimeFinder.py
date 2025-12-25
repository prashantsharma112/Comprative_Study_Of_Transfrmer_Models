import sys
from multiprocessing import Pool

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    start = int(input())
    end = int(input())
    chunks = int(input())
    pool = Pool(processes=chunks)
    futs = pool.map(isPrime, range(start, end + 1))
    total = 0
    for fut in futs:
        total += fut
    pool.close()
    pool.join()
    print(total)

if __name__ == '__main__':
    main()