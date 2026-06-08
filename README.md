# Weekly Coding #4 — Metro City Help Center

## Summary
Metro City Help Center needs a small support system to track staff actions, serve waiting citizens, validate request notes, and process service lines. This week's work implements **stack** (LIFO) and **queue** (FIFO) behavior using Python's `list` and `collections.deque`.

## How to run
```bash
pytest -q
```

## Complexity

### `ActionStack.pop`
- **Time: O(1)**
- Why: `list.pop()` with no index removes from the end — no shifting needed.

### `RequestQueue.dequeue`
- **Time: O(1)**
- Why: `deque.popleft()` removes from the front in constant time. A plain `list` would be O(n) here, which is why `deque` is used.

### `is_note_balanced`
- **Time: O(n)** where n = length of the note string
- Why: Each character is visited exactly once; stack push/pop are O(1).

### `process_request_line`
- **Time: O(n)** where n = number of citizens
- Why: Each citizen is enqueued once and dequeued once — two O(1) operations per person.

## Edge-case checklist
- [x] **Empty action stack** — `pop()` and `peek()` return `None`; `is_empty()` returns `True`
- [x] **Empty request queue** — `dequeue()` and `peek()` return `None`; `is_empty()` returns `True`
- [x] **Empty string for `is_note_balanced`** — the loop body never runs; the stack stays empty, so `True` is returned
- [x] **Note with no brackets** — no characters match `([{` or `}])`, stack stays empty, returns `True`
- [x] **Empty citizen list** — `process_request_line([])` returns `[]` immediately

## Assistance & sources
- AI used? **Y**
- What it helped with: code structure review and README formatting
- Other sources: Python docs — [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)