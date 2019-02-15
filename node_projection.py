from node import Node

class NodeProjection(Node):
    def __init__(self, columns):
        super().__init__()
        self.columns = columns

    def next(self):
        row = self.children[0].next()
        if row is None:
            return None
        return { col: row[col] for col in self.columns }

