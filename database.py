from constants import *
from node_file_scan import NodeFileScan
from node_test_scan import NodeTestScan
from node_projection import NodeProjection

def process(query):
    current_node = None
    root_node = None

    for statement in query:
        operator = statement[0]
        if (operator == PROJECTION):
            node = NodeProjection(statement[1:])

        elif (operator == FILE_SCAN):
            node = NodeFileScan('movies_head.csv')

        elif (operator == TEST_SCAN):
            node = NodeTestScan()

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

    root_node.close()

    return result

query = [
    [ PROJECTION, "title" ],
    [ FILE_SCAN ]
]

result = process(query)
[ print(row) for row in result]
