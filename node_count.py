from node import Node

class NodeCount(Node):
    def __init__(self):
        self.count = 0
        self.ran = False

    def next(self):
        if self.ran:
            return None

        row = self.child.next()
        while row is not None:
            self.count += 1
            row = self.child.next()

        self.ran = True
        return self.count
