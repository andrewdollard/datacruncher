from constants import EQUALS
from node import Node

class NodeSelection(Node):
    def __init__(self, args):
        self.column = args[0]
        self.comparator = args[1]
        self.value = args[2]

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


