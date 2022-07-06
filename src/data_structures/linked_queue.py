from typing import Optional
from data_structures import LinkedList


class LinkedQueue:
    def __init__(self) -> None:
        self._values = LinkedList([])

    def peek(self) -> Optional[int]:
        if self._values.length == 0:
            return None

        return self._values.access(0)

    def enqueue(self, value: int):
        self._values.insert(value, self._values.length)

    def dequeue(self) -> Optional[int]:
        if self._values.length == 0:
            return None

        value = self._values.access(0)
        self._values.delete(0)
        return value
