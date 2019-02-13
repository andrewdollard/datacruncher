from node import Node

class NodeSort(Node):
    def __init__(self, sortColumn):
        self.sortColumn = sortColumn
        self.items = []
        self.ran = False
        self.currentIdx = 0

    def next(self):
        if not self.ran:
            row = self.child.next()
            while row is not None:
                self.items.append(row)
                row = self.child.next()
            self.items.sort(key=lambda item: item[self.sortColumn])

        if self.currentIdx >= len(self.items):
            return None
        result = self.items[self.currentIdx]
        self.currentIdx += 1
        return result

