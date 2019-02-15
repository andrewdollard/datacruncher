from node import Node

class NodeFileScan(Node):
    def __init__(self, filename):
        super().__init__()
        self.file = None
        self.filename = filename
        self.reset()

    def next(self):
        row = self.file.readline()
        if row == '':
            return None
        row = row.strip().split(',')
        return { self.schema[i]: row[i] for i in range(len(self.schema)) }

    def reset(self):
        self.close()
        self.file = open(self.filename)
        self.schema = self.file.readline().strip().split(',')

    def close(self):
        if self.file is not None and not self.file.closed:
            self.file.close()
