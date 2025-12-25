import sys
import os
import time

def count_lines(files):
    total = 0
    for f in files:
        with open(f, 'r') as f:
            total += len(f.readlines())
    return total

if __name__ == '__main__':
    files = sys.argv[1:]
    total = 0
    for f in files:
        with open(f, 'r') as f:
            total += len(f.readlines())
    print(total)