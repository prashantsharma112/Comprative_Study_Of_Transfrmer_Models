import heapq
import threading

    def __init__(self, p, m):
        self.p = p
        self.m = m

    def __lt__(self, other):
        return other.p < self.p

def read_int_safe(sc):
    while True:
        try:
            return int(input())
        except ValueError:
            print("Invalid input. Enter a valid integer:")

def main():
    print("Enter number of events: ", end="")
    n = read_int_safe(input)

    pr = []

    print("Enter " + str(n) + " integer priorities:")
    for _ in range(n):
        pr.append(read_int_safe(input))

    q = []
    for i in range(n):
        heapq.heappush(q, E(pr[i], "E" + str(i)))

    def process_event(e):
        pass

    threads = []
    num_threads = min(4, n)
    for _ in range(num_threads):
        def worker():
            while q:
                try:
                    e = heapq.heappop(q)
                    process_event(e)
                except IndexError:
                    break
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Processed: " + str(n))

if __name__ == "__main__":
    main()