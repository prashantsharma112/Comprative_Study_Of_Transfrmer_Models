def main():
    sc = __import__('sys').stdin

    def next_int():
        return int(sc.readline().strip())

    def next_str():
        return sc.readline().strip()

    def next_ints():
        return [int(x) for x in sc.readline().strip().split()]

    def next_strs():
        return sc.readline().strip().split()

    t = next_int()
    ids = []
    keys = []
    for i in range(t):
        line = next_ints()
        id_val = line[0]
        ids.append(id_val)
        k = line[1]
        s = set()
        line2 = next_strs()
        for j in range(k):
            s.add(line2[j])
        keys.append(s)

    for i in range(t):
        status[ids[i]] = "COMMIT"

    for i in range(t):
        for j in range(i + 1, t):
            a = keys[i]
            b = keys[j]
            
            if any(k in b for k in a):
                status[ids[i]] = "CONFLICT"
                status[ids[j]] = "CONFLICT"
    
    sb = ""
    first = True
    for key, value in status.items():
        if not first:
            sb += " "
        first = False
        sb += str(key) + ":" + value

    print(sb)

if __name__ == "__main__":
    main()