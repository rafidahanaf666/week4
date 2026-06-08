from __future__ import annotations
from collections import deque


class ActionStack:
    """Stack of recent help-center actions using a Python list (LIFO)."""

    def __init__(self) -> None:
        self._items: list[str] = []

    def push(self, action: str) -> None:
        """Add an action to the top of the stack."""
        self._items.append(action)

    def pop(self) -> str | None:
        """Remove and return the top action, or None if the stack is empty."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> str | None:
        """Return the top action without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no actions."""
        return len(self._items) == 0


class RequestQueue:
    """Queue of waiting citizens using collections.deque (FIFO)."""

    def __init__(self) -> None:
        self._items: deque[str] = deque()

    def enqueue(self, name: str) -> None:
        """Add a citizen name to the back of the queue."""
        self._items.append(name)

    def dequeue(self) -> str | None:
        """Remove and return the front citizen, or None if the queue is empty."""
        if self.is_empty():
            return None
        return self._items.popleft()

    def peek(self) -> str | None:
        """Return the front citizen without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no waiting citizens."""
        return len(self._items) == 0


def is_note_balanced(note: str) -> bool:
    """Return True if all bracket pairs () [] {} are balanced correctly."""
    stack: list[str] = []
    pairs: dict[str, str] = {')': '(', ']': '[', '}': '{'}

    for ch in note:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def process_request_line(citizens: list[str]) -> list[str]:
    """Return citizens in the order they are served (FIFO)."""
    queue: deque[str] = deque(citizens)
    result: list[str] = []

    while queue:
        result.append(queue.popleft())

    return result


def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
    """Remove the most recent undo_count actions and return the rest."""
    stack = list(actions)
    for _ in range(undo_count):
        if stack:
            stack.pop()
    return stack