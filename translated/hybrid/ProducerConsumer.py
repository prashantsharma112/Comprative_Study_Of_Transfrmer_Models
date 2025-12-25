import sys
import time

items = []

for i in range(int(input())):
    items.append(input())

items.append("<<EOF>>")

q = ArrayBlockingQueue(10)
consumed = []

def producer():
    while True:
        try:
            q.put(items.pop())
        except:
            break

def consumer():
    while True:
        try:
            v = q.get()
            if v == "<<EOF>>":
                break
            else:
                consumed.append(v)
        except:
            break

producer()
consumer()

print(" ".join(consumed))