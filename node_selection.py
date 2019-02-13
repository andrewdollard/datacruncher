from constants import EQUALS
from node import Node

class NodeSelection(Node):
    def __init__(self, column, comparator, value):
        self.column = column
        self.comparator = comparator
        self.value = value

    def next(self):
        row = self.child.next()
        if row is None:
            return None

        while not self._compare(row[self.column], self.value, self.comparator):
            row = self.child.next()
            if row is None:
                return None

        return row

    def _compare(self, left, right, operator):
        if operator == EQUALS:
            return left == right


