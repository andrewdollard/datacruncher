from node import Node

class NodeProjection(Node):
    def __init__(self, columns):
        self.columns = columns

    def next(self):
        row = self.child.next()
        if row is None:
            return None
        return { col: row[col] for col in self.columns }

