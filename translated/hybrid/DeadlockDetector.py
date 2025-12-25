import sys

    def hasCycle(self, g):
        vis = set()
        stack = set()
        for node in g.keys():
            if self.dfs(node, g, vis, stack):
                return True
        return False

    def dfs(self, node, g, vis, stack):
        if node in stack:
            return True
        if node in vis:
            return False
        vis.add(node)
        stack.add(node)
        for nxt in g.get(node, []):
            if self.dfs(nxt, g, vis, stack):
                return True
        stack.remove(node)
        return False

if __name__ == '__main__':
    m = int(input())
    for _ in range(m):
        a, b = input().split()
        g.setdefault(a, []).append(b)
    print(DeadlockDetector().hasCycle(g) and 'DEADLOCK' or 'NO_DEADLOCK')