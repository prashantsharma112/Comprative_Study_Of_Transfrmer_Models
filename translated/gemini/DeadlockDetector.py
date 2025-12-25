def hasCycle(g):
    vis = set()
    stack = set()
    for node in g.keys():
        if dfs(node, g, vis, stack):
            return True
    return False

def dfs(node, g, vis, stack):
    if node in stack:
        return True
    if node in vis:
        return False
    vis.add(node)
    stack.add(node)
    for nxt in g.get(node, []):
        if dfs(nxt, g, vis, stack):
            return True
    stack.remove(node)
    return False

def main():
    import sys
    sc = sys.stdin
    m = int(sc.readline())
    for _ in range(m):
        a, b = sc.readline().split()
        if a not in g:
            g[a] = []
        g[a].append(b)

    print("DEADLOCK" if hasCycle(g) else "NO_DEADLOCK")

if __name__ == "__main__":
    main()