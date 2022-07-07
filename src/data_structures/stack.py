from typing import Optional


class Stack:
    def __init__(self) -> None:
        self._values = []

    def __len__(self) -> int:
        return len(self._values)

    def peek(self) -> Optional[int]:
        if len(self._values) == 0:
            return None

        return self._values[-1]

    def push(self, value: int) -> None:
        self._values.append(value)

    def pop(self) -> Optional[int]:
        if len(self._values) == 0:
            return None

        return self._values.pop()

    def is_empty(self) -> bool:
        return len(self) == 0
