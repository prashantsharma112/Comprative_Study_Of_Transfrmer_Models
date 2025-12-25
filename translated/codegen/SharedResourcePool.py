import sys

def main(argv):
    if len(argv) < 2:
        print("Usage: python -m SharedResourcePool <pool size>")
        return
    poolSize = int(argv[1])
    pool = ArrayBlockingQueue(poolSize)
    for i in range(poolSize):
        pool.put(i+1)
    print(pool.take())

if __name__ == "__main__":
    main(sys.argv)