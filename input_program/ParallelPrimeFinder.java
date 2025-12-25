
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.*;

public class ParallelPrimeFinder {
    static boolean isPrime(int n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        for (int i = 3; i * i <= n; i += 2) if (n % i == 0) return false;
        return true;
    }
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt();
        int chunks = sc.nextInt();
        sc.close();

        int range = end - start + 1;
        int chunkSize = Math.max(1, range / chunks);
        ExecutorService ex = Executors.newFixedThreadPool(Math.min(chunks, Runtime.getRuntime().availableProcessors()));
        List<Future<Integer>> futs = new ArrayList<>();
        int s = start;
        while (s <= end) {
            int e = Math.min(end, s + chunkSize - 1);
            final int ss = s, ee = e;
            futs.add(ex.submit(() -> {
                int c = 0;
                for (int i = ss; i <= ee; i++) if (isPrime(i)) c++;
                return c;
            }));
            s = e + 1;
        }
        int total = 0;
        for (Future<Integer> f : futs) total += f.get();
        ex.shutdown();
        System.out.println(total);
    }
}
