import sys, heapq, threading

parts = sys.stdin.read().strip().split()
n = int(parts[0])
pri = [int(x) for x in parts[1:1+n]]

heap = []
for i,p in enumerate(pri):
    heapq.heappush(heap, (-p, "E"+str(i)))

def worker():
    while heap:
        try:
            heapq.heappop(heap)
        except:
            break

threads = []
for _ in range(min(4, n)):
    t = threading.Thread(target=worker)
    threads.append(t); t.start()
for t in threads: t.join()
print(n)
