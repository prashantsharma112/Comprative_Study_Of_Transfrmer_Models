import sys
parts = sys.stdin.read().strip().split()
m = int(parts[0])
it = iter(parts[1:])
g = {}
for _ in range(m):
    a = next(it); b = next(it)
    g.setdefault(a, []).append(b)

visited = set(); stack = set()
def dfs(node):
    if node in stack: return True
    if node in visited: return False
    visited.add(node); stack.add(node)
    for nxt in g.get(node, []):
        if dfs(nxt): return True
    stack.remove(node); return False

res = any(dfs(n) for n in g.keys())
print("DEADLOCK" if res else "NO_DEADLOCK")
