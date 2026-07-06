# SYZYGY — Collatz Conjecture Oracle

A computational art piece that probes the depths of the Collatz conjecture through a brutalist-luxury interface. Named after the astronomical alignment of celestial bodies, SYZYGY aligns raw number theory with visceral web aesthetics.

## Architecture

```
┌─────────────────┐     HTTP/JSON      ┌──────────────────┐
│   index.html    │ ◄──────────────►   │  hailstone_api.py │
│ (Canvas + DOM)  │    CORS Enabled     │  (Port 8001)      │
└─────────────────┘                     └──────────────────┘
         ▲
         │ Type Contract
         ▼
┌─────────────────┐
│ api_contract.ts │
│ (TypeScript     │
│  Definitions)   │
└─────────────────┘
```

## Dependencies

- **Python 3.8+** — Standard library only (`http.server`, `functools`)
- **Modern Web Browser** — ES6 Modules, Canvas API, Fetch API
- **TypeScript 4.0+** *(optional, for type-checking the API contract)*

## Deployment Ritual

### 1. Invoke the Python Backend
```bash
python3 hailstone_api.py
```
The API will manifest on `http://localhost:8001`. The Collatz sequence length calculator uses `lru_cache` for memoization, achieving O(n) amortized complexity for the longest-sequence search.

### 2. Serve the Frontend
Any static file server suffices. Using Python's built-in:
```bash
python3 -m http.server 8000
```
Navigate to `http://localhost:8000`. The particle field initializes immediately; the API call triggers on button press or Enter key.

### 3. TypeScript Contract Verification (Optional)
```bash
tsc api_contract.ts --noEmit
```
Validates the API response shape against the `HailstoneArray` type `[number, number]`.

## API Specification

**Endpoint:** `GET /hailstone?limit=<positive_integer>`

**Response:** `[seed_number, sequence_length]`

**Example:**
```json
[77031, 351]
```

**Contract:** Referenced in `api_contract.ts` as `APIEndpoints.getHailstone.response`.

## Algorithmic Implementation

The Collatz (Hailstone) sequence length is computed via recursion with memoization:

```python
@lru_cache(maxsize=None)
def sequence_length(n):
    if n == 1: return 1
    if n % 2 == 0: return 1 + sequence_length(n // 2)
    else: return 1 + sequence_length(3 * n + 1)
```

This avoids stack overflow for large limits through Python's recursion limit handling, while `lru_cache` ensures each integer's length is computed exactly once.

## Sources

- Lagarias, J. C. (1985). The 3x+1 problem and its generalizations. *The American Mathematical Monthly*, 92(1), 3–23. https://doi.org/10.1080/00029890.1985.11971528
- Tao, T. (2019). Almost all Collatz orbits attain almost bounded values. *arXiv preprint arXiv:1909.03562*.
```
