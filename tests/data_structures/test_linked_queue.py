import pytest
from data_structures import LinkedList, LinkedQueue


@pytest.fixture
def multi_queue():
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue


class TestInit:
    def test_default(self):
        queue = LinkedQueue()
        assert queue._values == LinkedList([])


class TestPeek:
    def test_empty(self):
        queue = LinkedQueue()
        assert queue.peek() is None

    def test_single_value(self):
        queue = LinkedQueue()
        queue._values = LinkedList([1])
        assert queue.peek() == 1

    def test_multi_values(self):
        queue = LinkedQueue()
        queue._values = LinkedList([1, 2, 3])
        assert queue.peek() == 1


class TestEnqueue:
    def test_single_enqueue(self):
        queue = LinkedQueue()
        queue.enqueue(1)
        assert queue.peek() == 1

    def test_multi_enqueue(self, multi_queue):
        stack = multi_queue
        assert stack.peek() == 1


class TestDequeue:
    def test_empty_dequeue(self):
        queue = LinkedQueue()
        assert queue.dequeue() is None
        assert queue.peek() is None

    def test_single_dequeue_one_value(self):
        queue = LinkedQueue()
        queue.enqueue(1)
        assert queue.dequeue() == 1
        assert queue.dequeue() is None
        assert queue.peek() is None

    def test_single_dequeue_multi_values(self, multi_queue):
        queue = multi_queue
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() is None
        assert queue.peek() is None
