import java.util.HashMap;
import java.util.Map;

public class HailstoneSequence {
    
    private static Map<Long, Long> cache = new HashMap<>();
    
    public static long[] hailstoneSequence(long limit) {
        long maxNumber = 0;
        long maxLength = 0;
        
        for (long i = 1; i < limit; i++) {
            long currentLength = sequenceLength(i);
            if (currentLength > maxLength) {
                maxLength = currentLength;
                maxNumber = i;
            }
        }
        
        return new long[]{maxNumber, maxLength};
    }
    
    private static long sequenceLength(long n) {
        if (n == 1) return 1;
        if (cache.containsKey(n)) return cache.get(n);
        
        long length;
        if (n % 2 == 0) {
            length = 1 + sequenceLength(n / 2);
        } else {
            length = 1 + sequenceLength(3 * n + 1);
        }
        
        cache.put(n, length);
        return length;
    }
}
