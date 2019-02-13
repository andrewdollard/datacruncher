from node import Node

class NodeDistinct(Node):
    def __init__(self):
        self.counts = set()
        self.ran = False
        self.idx = 0

    def next(self):
        row = self.child.next()
        if row is None:
            return None

        hashed = frozenset(row.items())
        while hashed in self.counts:
            row = self.child.next()
            if row is None:
                return None
            hashed = frozenset(row.items())

        self.counts.add(hashed)
        return row


