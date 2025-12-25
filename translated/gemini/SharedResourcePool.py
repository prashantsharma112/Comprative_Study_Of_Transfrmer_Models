import threading
import queue
import time

def main():
    sc = input().split()
    poolSize = int(sc[0])
    clientThreads = int(sc[1])

    pool = queue.Queue(maxsize=poolSize)
    for i in range(poolSize):
        pool.put(i + 1)
    served = 0
    served_lock = threading.Lock()

    def client_task():
        nonlocal served
        try:
            r = pool.get()
            time.sleep(0.01)
            pool.put(r)
            with served_lock:
                served += 1
        except Exception:
            pass

    clients = []
    for i in range(clientThreads):
        client = threading.Thread(target=client_task)
        clients.append(client)
        client.start()

    for t in clients:
        t.join()

    print(served)

if __name__ == "__main__":
    main()