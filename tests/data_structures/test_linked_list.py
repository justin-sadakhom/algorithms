import pytest
from data_structures import LinkedList


@pytest.fixture
def empty_list():
    return LinkedList([])


class TestInit:
    def test_empty_list(self, empty_list):
        lst = empty_list
        assert lst.head is None
        assert lst.length == 0

    def test_one_element(self):
        lst = LinkedList([1])
        assert lst.head.value == 1
        assert lst.head.next is None
        assert lst.length == 1

    def test_two_elements(self):
        lst = LinkedList([1, 2])
        assert lst.head.value == 1
        assert lst.head.next.value == 2
        assert lst.head.next.next is None
        assert lst.length == 2


class TestValues:
    def test_empty_list(self, empty_list):
        lst = empty_list
        assert lst.values() == []

    def test_one_element(self):
        lst = LinkedList([1])
        assert lst.values() == [1]

    def test_two_elements(self):
        lst = LinkedList([1, 2])
        assert lst.values() == [1, 2]


class TestInsert:
    def test_negative_pos(self, empty_list):
        lst = empty_list
        lst.insert(0, -1)
        assert lst.values() == []

    def test_lengthy_pos(self, empty_list):
        lst = empty_list
        lst.insert(0, 1)
        assert lst.values() == []

    def test_empty_list(self, empty_list):
        lst = empty_list
        lst.insert(0, 0)
        assert lst.values() == [0]

    def test_insert_head(self):
        lst = LinkedList([1])
        lst.insert(0, 0)
        assert lst.values() == [0, 1]

    def test_insert_tail(self):
        lst = LinkedList([1])
        lst.insert(2, 1)
        assert lst.values() == [1, 2]

    def test_insert_middle(self):
        lst = LinkedList([1, 3])
        lst.insert(2, 1)
        assert lst.values() == [1, 2, 3]
