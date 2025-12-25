
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class ProducerConsumer {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<String> items = new ArrayList<>();
        for (int i = 0; i < n; i++) items.add(sc.next());
        sc.close();

        BlockingQueue<String> q = new ArrayBlockingQueue<>(10);
        List<String> consumed = new ArrayList<>();

        Thread producer = new Thread(() -> {
            try {
                for (String it : items) q.put(it);
                q.put("<<EOF>>");
            } catch (InterruptedException ignored) {}
        });

        Thread consumer = new Thread(() -> {
            try {
                while (true) {
                    String v = q.take();
                    if (v.equals("<<EOF>>")) break;
                    synchronized (consumed) { consumed.add(v); }
                }
            } catch (InterruptedException ignored) {}
        });

        producer.start();
        consumer.start();
        producer.join();
        consumer.join();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < consumed.size(); i++) {
            if (i > 0) sb.append(" ");
            sb.append(consumed.get(i));
        }
        System.out.println(sb.toString());
    }
}
