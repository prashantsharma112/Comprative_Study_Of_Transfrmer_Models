import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class EventDispatcher {
    static class E implements Comparable<E> {
        int p;
        String m;
        E(int p, String m) {
            this.p = p;
            this.m = m;
        }
        public int compareTo(E o) {
            return Integer.compare(o.p, this.p);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read N safely
        System.out.print("Enter number of events: ");
        int n = readIntSafe(sc);

        List<Integer> pr = new ArrayList<>();

        System.out.println("Enter " + n + " integer priorities:");
        for (int i = 0; i < n; i++) {
            pr.add(readIntSafe(sc));
        }

        sc.close();

        PriorityQueue<E> q = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            q.add(new E(pr.get(i), "E" + i));
        }

        ExecutorService ex = Executors.newFixedThreadPool(Math.min(4, n));

        while (!q.isEmpty()) {
            E e = q.poll();
            ex.submit(() -> {
                // simulate processing
            });
        }

        ex.shutdown();
        System.out.println("Processed: " + n);
    }

    // Safe integer reader
    private static int readIntSafe(Scanner sc) {
        while (!sc.hasNextInt()) {
            System.out.println("Invalid input. Enter a valid integer:");
            sc.next();
        }
        return sc.nextInt();
    }
}
