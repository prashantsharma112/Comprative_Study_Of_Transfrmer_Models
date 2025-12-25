import sys
import time

poolSize = int(input())
clientThreads = int(input())

pool = []
for i in range(poolSize):
    pool.append(i+1)

served = 0

for i in range(clientThreads):
    t = Thread(target=lambda: pool.append(pool.pop()))
    t.start()

for t in clients:
    t.join()

print(served)