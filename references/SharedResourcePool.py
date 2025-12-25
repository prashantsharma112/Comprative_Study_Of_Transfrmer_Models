import sys, queue, threading, time

parts = sys.stdin.read().strip().split()
poolSize = int(parts[0]); clientThreads = int(parts[1])

pool = queue.Queue()
for i in range(1, poolSize+1):
    pool.put(i)
served = 0
served_lock = threading.Lock()

def client():
    global served
    r = pool.get()
    time.sleep(0.01)
    pool.put(r)
    with served_lock:
        served += 1

threads = []
for _ in range(clientThreads):
    t = threading.Thread(target=client)
    threads.append(t)
    t.start()
for t in threads: t.join()
print(served)
