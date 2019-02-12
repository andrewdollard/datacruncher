from node import Node

class NodeFileScan(Node):
    def __init__(self, args):
        self.file = open(args[0])
        self.schema = self.file.readline().strip().split(',')

    def next(self):
        row = self.file.readline()
        if row == '':
            return None
        row = row.strip().split(',')
        return { self.schema[i]: row[i] for i in range(len(self.schema)) }

    def close(self):
        self.file.close()