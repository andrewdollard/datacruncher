from node import Node

class NodeAverage(Node):
    def __init__(self):
        self.sum = 0
        self.count = 0
        self.ran = False

    def next(self):
        if self.ran:
            return None

        row = self.child.next()
        while row is not None:
            self.sum += float(list(row.values())[0])
            self.count += 1
            row = self.child.next()

        if self.count == 0:
            return None

        self.ran = True
        return self.sum / self.count
