from node import Node

class NodeTestScan(Node):
    DATA = [
        {'movieId': 1, 'title': 'foo', 'genres': 'action'},
        {'movieId': 2, 'title': 'bar', 'genres': 'action'},
        {'movieId': 3, 'title': 'baz', 'genres': 'action'},
    ]

    def __init__(self):
        super().__init__()
        self.idx = 3

    def next(self):
        self.idx -= 1
        if (self.idx < 0):
            return None
        return self.DATA[self.idx]

