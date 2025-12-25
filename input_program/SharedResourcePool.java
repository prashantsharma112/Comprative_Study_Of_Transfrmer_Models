
import java.util.Scanner;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class SharedResourcePool {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int poolSize = sc.nextInt();
        int clientThreads = sc.nextInt();
        sc.close();

        BlockingQueue<Integer> pool = new ArrayBlockingQueue<>(poolSize);
        for (int i = 0; i < poolSize; i++) pool.put(i+1);
        AtomicInteger served = new AtomicInteger(0);

        Thread[] clients = new Thread[clientThreads];
        for (int i = 0; i < clientThreads; i++) {
            clients[i] = new Thread(() -> {
                try {
                    Integer r = pool.take();
                    Thread.sleep(10);
                    pool.put(r);
                    served.incrementAndGet();
                } catch (Exception ignored) {}
            });
            clients[i].start();
        }
        for (Thread t : clients) t.join();
        System.out.println(served.get());
    }
}
