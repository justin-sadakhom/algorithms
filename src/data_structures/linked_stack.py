from typing import Optional
from data_structures import LinkedList


class LinkedStack:
    def __init__(self) -> None:
        self._values = LinkedList([])

    def peek(self) -> Optional[int]:
        if self._values.length == 0:
            return None

        return self._values.access(self._values.length - 1)

    def push(self, value: int) -> None:
        self._values.insert(value, self._values.length)

    def pop(self) -> Optional[int]:
        if self._values.length == 0:
            return None

        value = self._values.access(self._values.length - 1)
        self._values.delete(self._values.length - 1)
        return value
