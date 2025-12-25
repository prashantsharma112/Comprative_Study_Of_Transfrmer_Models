import sys

def main():
    t = int(input())
    ids = []
    keys = []
    for i in range(t):
        id = int(input())
        k = int(input())
        s = set()
        for j in range(k):
            s.add(input())
        keys.append(s)
        ids.append(id)
    sc = sys.stdin
    for i in range(t):
        for j in range(i+1, t):
            a = keys[i]
            b = keys[j]
            for k in a:
                if k in b:
                    ids[i] = "CONFLICT"
                    ids[j] = "CONFLICT"
                    break
    sb = ""
    first = True
    for e in sorted(zip(ids, keys)):
        if not first: sb += " "
        first = False
        sb += str(e[0]) + ":" + str(e[1])
    print(sb)

if __name__ == "__main__":
    main()