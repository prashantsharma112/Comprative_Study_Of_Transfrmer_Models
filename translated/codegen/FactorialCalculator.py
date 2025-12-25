import sys

def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)

if __name__ == "__main__":
    sys.exit(factorial(int(input())))