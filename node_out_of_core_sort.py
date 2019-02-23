from node import Node

class NodeOutOfCoreSort(Node):

    def __init__(self, filename):
        self.file = None
        self.filename = filename
        self.reset()

    def read_page(self):
        output = self.file.readlines(65536)
        if output == []:
            return None

        lines = [line.strip().split(',') for line in output]
        res = [ { self.schema[i]: row[i] for i in range(len(self.schema)) } for row in lines  ]
        return res

    def reset(self):
        self.close()
        self.file = open(self.filename)
        self.schema = self.file.readline().strip().split(',')

    def close(self):
        if self.file is not None and not self.file.closed:
            self.file.close()

node = NodeOutOfCoreSort("data/ratings.csv")

page = node.read_page()
while page is not None:
    page = node.read_page()


