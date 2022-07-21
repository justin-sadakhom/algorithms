import pytest
from data_structures import BinaryTree


@pytest.fixture
def empty_tree():
    return BinaryTree()


@pytest.fixture
def tree_without_children():
    return BinaryTree(1)


@pytest.fixture
def tree_with_children():
    tree = BinaryTree(4)
    values = [1, 2, 3, 5]

    for value in values:
        tree.insert(value)

    return tree


@pytest.fixture
def tree_left_child():
    tree = BinaryTree(1)
    tree.insert(0)
    return tree


@pytest.fixture
def tree_right_child():
    tree = BinaryTree(1)
    tree.insert(2)
    return tree


class TestInit:
    def test_empty_tree(self):
        tree = BinaryTree()
        assert not tree.root

    def test_no_children(self):
        tree = BinaryTree(1)
        assert tree.root.value == 1
        assert not tree.root.left
        assert not tree.root.right


class TestEq:
    def test_empty_tree(self, empty_tree):
        tree_1 = empty_tree
        tree_2 = BinaryTree()

        assert tree_1 == tree_2

    def test_no_children(self, tree_without_children):
        tree_1 = tree_without_children
        tree_2 = BinaryTree(1)

        assert tree_1 == tree_2

    def test_with_children(self, tree_without_children):
        tree_1 = tree_without_children
        tree_1.insert(2)

        tree_2 = BinaryTree(1)
        tree_2.insert(2)

        assert tree_1 == tree_2


class TestInsert:
    def test_empty_tree(self, empty_tree, tree_without_children):
        tree = empty_tree
        tree.insert(1)

        assert tree == tree_without_children

    def test_left_insert(self, tree_without_children, tree_left_child):
        tree = tree_without_children
        tree.insert(0)

        assert tree == tree_left_child

    def test_right_insert(self, tree_without_children, tree_right_child):
        tree = tree_without_children
        tree.insert(2)

        assert tree == tree_right_child

    def test_multi_insert(self, tree_with_children):
        tree = BinaryTree(4)
        values = [1, 2, 3, 5]

        for value in values:
            tree.insert(value)

        assert tree == tree_with_children
