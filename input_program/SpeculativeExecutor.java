
import java.util.*;
import java.util.concurrent.*;

public class SpeculativeExecutor {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        List<Integer> ids = new ArrayList<>();
        List<Set<String>> keys = new ArrayList<>();
        for (int i = 0; i < t; i++) {
            int id = sc.nextInt(); ids.add(id);
            int k = sc.nextInt();
            Set<String> s = new HashSet<>();
            for (int j = 0; j < k; j++) s.add(sc.next());
            keys.add(s);
        }
        sc.close();

        Map<Integer,String> status = new LinkedHashMap<>();
        for (int i = 0; i < t; i++) status.put(ids.get(i), "COMMIT");

        for (int i = 0; i < t; i++) {
            for (int j = i+1; j < t; j++) {
                Set<String> a = keys.get(i), b = keys.get(j);
                for (String k : a) if (b.contains(k)) { status.put(ids.get(i), "CONFLICT"); status.put(ids.get(j), "CONFLICT"); break; }
            }
        }
        StringBuilder sb = new StringBuilder();
        boolean first = true;
        for (Map.Entry<Integer,String> e : status.entrySet()) {
            if (!first) sb.append(" ");
            first = false;
            sb.append(e.getKey()).append(":").append(e.getValue());
        }
        System.out.println(sb.toString());
    }
}
