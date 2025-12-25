import threading
import queue

def main():
    sc = input().split()
    n = int(sc[0])
    items = sc[1:]

    q = queue.Queue(maxsize=10)
    consumed = []

    def producer():
        try:
            for it in items:
                q.put(it)
            q.put("<<EOF>>")
        except Exception:
            pass

    def consumer():
        try:
            while True:
                v = q.get()
                if v == "<<EOF>>":
                    break
                with consumed:
                    consumed.append(v)
        except Exception:
            pass

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()

    sb = ""
    for i in range(len(consumed)):
        if i > 0:
            sb += " "
        sb += consumed[i]
    print(sb)

if __name__ == "__main__":
    main()