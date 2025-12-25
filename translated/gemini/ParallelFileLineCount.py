import concurrent.futures
import os

def main():
    n = int(input())
    files = input().split()[:n]

    def count_lines(filename):
        c = 0
        try:
            with open(filename, 'r') as f:
                for _ in f:
                    c += 1
        except Exception:
            pass
        return c

    total = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(n, os.cpu_count())) as executor:
        futures = [executor.submit(count_lines, f) for f in files]
        for future in concurrent.futures.as_completed(futures):
            total += future.result()
    print(total)

if __name__ == "__main__":
    main()