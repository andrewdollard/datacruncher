from node import Node

class NodeCount(Node):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.ran = False

    def next(self):
        if self.ran:
            return None

        row = self.children[0].next()
        while row is not None:
            self.count += 1
            row = self.children[0].next()

        self.ran = True
        return self.count
