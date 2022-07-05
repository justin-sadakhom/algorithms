from typing import List


class _Node:
    next = None

    def __init__(self, value: int) -> None:
        self.value = value


class LinkedList:
    head = None
    length = 0

    def __init__(self, values: List[int]) -> None:
        if len(values) > 0:
            self.head = _Node(values[0])
            self.length = len(values)
            curr = self.head

            for i in range(1, len(values)):
                curr.next = _Node(values[i])
                curr = curr.next

    def values(self) -> List[int]:
        result = []
        curr = self.head

        while curr is not None:
            result.append(curr.value)
            curr = curr.next

        return result

    def insert(self, value: int, pos: int) -> None:
        if pos < 0 or pos > self.length:
            return
        if pos == 0:
            curr = _Node(value)
            curr.next = self.head
            self.head = curr
            return

        curr = self.head
        prev = None
        count = 0

        while count < pos:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = _Node(value)
        prev.next.next = curr

    def delete(self, pos: int) -> None:
        if pos < 0 or pos >= self.length:
            return
        if pos == 0:
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        count = 0

        while count < pos:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = curr.next
