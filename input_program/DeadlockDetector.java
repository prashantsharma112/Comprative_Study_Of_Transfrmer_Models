
import java.util.*;

public class DeadlockDetector {
    public static boolean hasCycle(Map<String,List<String>> g) {
        Set<String> vis = new HashSet<>(), stack = new HashSet<>();
        for (String node : g.keySet()) if (dfs(node, g, vis, stack)) return true;
        return false;
    }
    private static boolean dfs(String node, Map<String,List<String>> g, Set<String> vis, Set<String> stack) {
        if (stack.contains(node)) return true;
        if (vis.contains(node)) return false;
        vis.add(node); stack.add(node);
        for (String nxt : g.getOrDefault(node, Collections.emptyList())) if (dfs(nxt, g, vis, stack)) return true;
        stack.remove(node); return false;
    }

    public static void main(String[] args) throws Exception {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int m = sc.nextInt();
        Map<String,List<String>> g = new HashMap<>();
        for (int i = 0; i < m; i++) {
            String a = sc.next(); String b = sc.next();
            g.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
        }
        sc.close();
        System.out.println(hasCycle(g) ? "DEADLOCK" : "NO_DEADLOCK");
    }
}
