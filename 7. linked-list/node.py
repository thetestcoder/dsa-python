class Node:
    __slot__ = '_element', '_next'

    def __init__(self, element, next):
        self._element= element
        self._next = next