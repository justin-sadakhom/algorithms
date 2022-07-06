from typing import List, Optional


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

    def access(self, index: int) -> Optional[int]:
        if index < 0 or index >= self.length:
            return None

        count = 0
        curr = self.head

        while count < index:
            curr = curr.next
            count += 1

        return curr.value

    def insert(self, value: int, index: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            curr = _Node(value)
            curr.next = self.head
            self.head = curr
            return

        curr = self.head
        prev = None
        count = 0

        while count < index:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = _Node(value)
        prev.next.next = curr

    def delete(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        count = 0

        while count < index:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = curr.next
