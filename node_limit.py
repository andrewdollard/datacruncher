from node import Node

class NodeLimit(Node):
    def __init__(self, limit):
        self.limit = limit

    def next(self):
        if self.limit == 0:
            return None;

        self.limit -= 1
        return self.child.next()
