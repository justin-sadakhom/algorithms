import pytest
from data_structures import LinkedList, LinkedStack


@pytest.fixture
def multi_stack():
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack


class TestInit:
    def test_default(self):
        stack = LinkedStack()
        assert stack._values == LinkedList([])


class TestPeek:
    def test_empty(self):
        stack = LinkedStack()
        assert stack.peek() is None

    def test_single_value(self):
        stack = LinkedStack()
        stack._values = LinkedList([1])
        assert stack.peek() == 1

    def test_multi_values(self):
        stack = LinkedStack()
        stack._values = LinkedList([1, 2, 3])
        assert stack.peek() == 3


class TestPush:
    def test_single_push(self):
        stack = LinkedStack()
        stack.push(1)
        assert stack.peek() == 1

    def test_multi_push(self, multi_stack):
        stack = multi_stack
        assert stack.peek() == 3


class TestPop:
    def test_empty_pop(self):
        stack = LinkedStack()
        assert stack.pop() is None
        assert stack.peek() is None

    def test_single_pop_one_value(self):
        stack = LinkedStack()
        stack.push(1)
        assert stack.pop() == 1
        assert stack.pop() is None
        assert stack.peek() is None

    def test_single_pop_multi_values(self, multi_stack):
        stack = multi_stack
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.pop() is None
        assert stack.peek() is None
