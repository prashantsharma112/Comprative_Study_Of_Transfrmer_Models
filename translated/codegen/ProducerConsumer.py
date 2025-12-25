import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python ProducerConsumer.py <number of items>")
        sys.exit(1)

    n = int(input())
    items = []
    for i in range(n):
        items.append(sys.argv[2 + i])

    print("Producing " + str(n) + " items")
    for i in range(n):
        print("\t" + items.get(i))

if __name__ == "__main__":
    main()