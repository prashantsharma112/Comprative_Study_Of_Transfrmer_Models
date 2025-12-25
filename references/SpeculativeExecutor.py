import sys
parts = sys.stdin.read().strip().split()
it = iter(parts)
t = int(next(it))
ids = []
keys = []
for _ in range(t):
    idd = int(next(it)); ids.append(idd)
    k = int(next(it))
    s = set()
    for _ in range(k):
        s.add(next(it))
    keys.append(s)

status = {idd:"COMMIT" for idd in ids}
for i in range(t):
    for j in range(i+1, t):
        if keys[i] & keys[j]:
            status[ids[i]] = "CONFLICT"
            status[ids[j]] = "CONFLICT"

out = " ".join(f"{k}:{status[k]}" for k in ids)
print(out)

