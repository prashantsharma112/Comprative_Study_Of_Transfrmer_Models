import sys

def main():
    N = input()
    print("--- Table of " + N + " ---")
    for i in range(1, N + 1):
        print("x " + i + " = " + (N * i))
    print("--- End of table ---")

if __name__ == "__main__":
    main()