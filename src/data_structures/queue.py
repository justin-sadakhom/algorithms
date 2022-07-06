from typing import Optional


class Queue:
    def __init__(self) -> None:
        self._values = []

    def peek(self) -> Optional[int]:
        if len(self._values) == 0:
            return None

        return self._values[0]

    def enqueue(self, value: int) -> None:
        self._values.append(value)

    def dequeue(self) -> Optional[int]:
        if len(self._values) == 0:
            return None

        return self._values.pop(0)
