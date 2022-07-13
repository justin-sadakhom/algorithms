from __future__ import annotations
from typing import Optional


class _TreeNode:
    value: int
    left: Optional[_TreeNode]
    right: Optional[_TreeNode]

    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.left == other.left and self.right == other.right

    def insert(self, value: int) -> None:
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = _TreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = _TreeNode(value)

    def copy(self, other: _TreeNode) -> None:
        self.value = other.value
        self.left = other.left
        self.right = other.right

    # def _delete_root(self) -> _TreeNode:
    #     if not self.right:
    #


class BinaryTree:
    root: Optional[_TreeNode]

    def __init__(self, value: Optional[int] = None) -> None:
        if not value:
            self.root = None
        else:
            self.root = _TreeNode(value)

    def __eq__(self, other) -> bool:
        return self.root == other.root

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = _TreeNode(value)
        else:
            self.root.insert(value)
