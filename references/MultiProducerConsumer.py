import sys, queue, threading, time

parts = sys.stdin.read().strip().split()
producers = int(parts[0]); consumers = int(parts[1]); itemsPerProducer = int(parts[2])

q = queue.Queue(maxsize=20)
consumed = 0
consumed_lock = threading.Lock()

def producer(pid):
    for j in range(itemsPerProducer):
        q.put(pid * 1000000 + j)

def consumer():
    global consumed
    while True:
        try:
            v = q.get(timeout=0.05)
            with consumed_lock:
                consumed += 1
                if consumed >= producers * itemsPerProducer:
                    return
        except:
            with consumed_lock:
                if consumed >= producers * itemsPerProducer:
                    return
            time.sleep(0.01)

for i in range(producers):
    threading.Thread(target=producer, args=(i,)).start()
for _ in range(consumers):
    threading.Thread(target=consumer).start()

while True:
    with consumed_lock:
        if consumed >= producers * itemsPerProducer:
            print(consumed)
            break
