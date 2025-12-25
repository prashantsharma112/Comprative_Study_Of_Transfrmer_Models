
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.concurrent.*;

public class FibonacciCache {
    private static final ConcurrentMap<Integer, Long> cache = new ConcurrentHashMap<>();
    static {
        cache.put(0, 0L);
        cache.put(1, 1L);
    }
    public static long fib(int n) {
        Long v = cache.get(n);
        if (v != null) return v;
        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long c = a + b;
            a = b; b = c;
        }
        cache.putIfAbsent(n, b);
        return cache.get(n);
    }
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        List<Integer> vals = new ArrayList<>();
        for (int i = 0; i < m; i++) vals.add(sc.nextInt());
        sc.close();

        ExecutorService ex = Executors.newFixedThreadPool(Math.min(m, Runtime.getRuntime().availableProcessors()));
        List<Future<Long>> futs = new ArrayList<>();
        for (int v : vals) futs.add(ex.submit(() -> fib(v)));
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < futs.size(); i++) {
            if (i > 0) sb.append(" ");
            sb.append(futs.get(i).get());
        }
        ex.shutdown();
        System.out.println(sb.toString());
    }
}
