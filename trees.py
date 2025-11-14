"""Trees

Provides a simple binary tree object

"""
from collections.abc import Iterable


class Node:
    """Internal element for a tree, designed to be recursive"""
    def __init__(self, key, parent=None):
        self.key = key
        self._parent = parent
        self._left = None
        self._right = None

    def __repr__(self) -> str:
        if self._left is None and self._right is None:
            return f'{self.key}'
        return f'{self.key} ({self._left}, {self._right})'

    # Implement dunder methods to overload the relational boolean operators
    # Dataclasses can be used to automatically generate methods like these

    def __eq__(self, other) -> bool:
        return self.key == other

    def __lt__(self, other) -> bool:
        return self.key < other

    def __gt__(self, other) -> bool:
        return self.key > other

    def __le__(self, other) -> bool:
        return self.key <= other

    def __ge__(self, other) -> bool:
        return self.key >= other


    # Methods used to recursively manipulate the Tree
    
    def _insert(self, key) -> None:
        """Recursive function for adding a key to the Tree"""
        if key == self:
            pass
        elif key < self and self._left is not None:
            self._left._insert(key)
        elif key < self:
            self._left = Node(key, self)
        elif key > self and self._right is not None:
            self._right._insert(key)
        elif key > self:
            self._right = Node(key, self)

class Tree:
    def __init__(self, iterable: Iterable=()):
        self._root: None | Node = None
        for item in iterable:
            self.insert(item)

    def __repr__(self) -> str:
        return repr(self._root)

    # Public Methods

    def insert(self, key) -> None:
        """Inserts a key into the tree if it does not already exit"""
        if self._root is None:
            self._root = Node(key)
        else:
            self._root._insert(key)
