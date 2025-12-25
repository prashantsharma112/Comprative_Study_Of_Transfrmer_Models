
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.*;

public class ParallelFileLineCount {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<String> files = new ArrayList<>();
        for (int i = 0; i < n; i++) files.add(sc.next());
        sc.close();

        ExecutorService ex = Executors.newFixedThreadPool(Math.min(n, Runtime.getRuntime().availableProcessors()));
        List<Future<Integer>> futs = new ArrayList<>();
        for (String f : files) {
            futs.add(ex.submit(() -> {
                int c = 0;
                try (BufferedReader br = new BufferedReader(new FileReader(f))) {
                    while (br.readLine() != null) c++;
                } catch (Exception ignored) {}
                return c;
            }));
        }
        int total = 0;
        for (Future<Integer> f : futs) total += f.get();
        ex.shutdown();
        System.out.println(total);
    }
}
