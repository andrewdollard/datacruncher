PROJECTION = 'projection'
SELECTION = 'selection'
TEST_SCAN = 'test_scan'
FILE_SCAN = 'file_scan'

class TestScan:
    DATA = [
        {'movieId': 1, 'title': 'foo', 'genres': 'action'},
        {'movieId': 2, 'title': 'bar', 'genres': 'action'},
        {'movieId': 3, 'title': 'baz', 'genres': 'action'},
    ]

    def __init__(self):
        self.idx = 3

    def next(self):
        self.idx -= 1
        if (self.idx < 0):
            return None
        return self.DATA[self.idx]

class FileScan:
    def __init__(self, filename):
        self.file = open(filename)
        self.schema = self.file.readline().strip().split(',')

    def next(self):
        row = self.file.readline()
        if row == '':
            return None
        row = row.strip().split(',')
        return { self.schema[i]: row[i] for i in range(len(self.schema)) }

class Projection:
    def __init__(self, columns):
        self.columns = columns

    def set_child(self, child_node):
        self.child = child_node

    def next(self):
        row = self.child.next()
        if row is None:
            return None
        return { col: row[col] for col in self.columns }


def process(query):
    current_node = None
    root_node = None
    for statement in query:
        operator = statement[0]
        if (operator == PROJECTION):
            node = Projection(statement[1:])
        elif (operator == FILE_SCAN):
            node = FileScan('movies_head.csv')
        elif (operator == TEST_SCAN):
            node = TestScan()
        if root_node is None:
            root_node = node
            current_node = node
        else:
            current_node.set_child(node)
            current_node = node
    result = []
    row = root_node.next()
    while row is not None:
        result.append(row)
        row = root_node.next()
    return result

query = [
    [ PROJECTION, "title" ],
    [ FILE_SCAN ]
]

result = process(query)
[ print(row) for row in result]
