function hailstoneSequence(limit) {
    const cache = new Map();
    
    function sequenceLength(n) {
        if (n === 1) return 1;
        if (cache.has(n)) return cache.get(n);
        
        let length;
        if (n % 2 === 0) {
            length = 1 + sequenceLength(n / 2);
        } else {
            length = 1 + sequenceLength(3 * n + 1);
        }
        
        cache.set(n, length);
        return length;
    }
    
    let maxNumber = 0;
    let maxLength = 0;
    
    for (let i = 1; i < limit; i++) {
        const currentLength = sequenceLength(i);
        if (currentLength > maxLength) {
            maxLength = currentLength;
            maxNumber = i;
        }
    }
    
    return [maxNumber, maxLength];
}
