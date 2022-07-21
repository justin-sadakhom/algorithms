from __future__ import annotations
from typing import Optional, Tuple


def _delete_min(root: _TreeNode) -> Tuple[int, _TreeNode]:
    if not root.left:
        return root.value, root.right

    result = _delete_min(root.left)
    return result[0], root


def _delete(root: _TreeNode, value: int) -> _TreeNode:
    if value < root.value:
        root.left = _delete(root.left, value)
    elif value > root.value:
        root.right = _delete(root.right, value)
    else:
        if not root.left:
            root = root.right
        elif not root.right:
            root = root.left
        else:
            root = _delete_min(root)[1]

    return root


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

    def delete(self, value: int) -> None:
        _delete(self, value)


class BinaryTree:
    root: Optional[_TreeNode]

    def __init__(self, value: Optional[int] = None) -> None:
        if not value:
            self.root = None
        else:
            self.root = _TreeNode(value)

    def __eq__(self, other) -> bool:
        if not self.root:
            return not other.root

        return self.root == other.root

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = _TreeNode(value)
        else:
            self.root.insert(value)
            
    def delete(self, value: int) -> None:
        if not self.root:
            return

        self.root.delete(value)
