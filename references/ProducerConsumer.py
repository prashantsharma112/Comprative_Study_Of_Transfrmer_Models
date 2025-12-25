import queue, threading, sys

n = int(sys.stdin.readline().strip())
items = []
for _ in range(n):
    items.append(sys.stdin.readline().strip())

q = queue.Queue(maxsize=10)
consumed = []

def producer():
    for it in items:
        q.put(it)
    q.put("<<EOF>>")

def consumer():
    while True:
        v = q.get()
        if v == "<<EOF>>":
            break
        consumed.append(v)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
print(" ".join(consumed))
