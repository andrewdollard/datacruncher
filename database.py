from constants import *
from node_average import NodeAverage
from node_count import NodeCount
from node_file_scan import NodeFileScan
from node_limit import NodeLimit
from node_projection import NodeProjection
from node_selection import NodeSelection
from node_test_scan import NodeTestScan

def process(query):
    current_node = None
    root_node = None

    for statement in query:
        operator = statement[0]
        if (operator == PROJECTION):
            node = NodeProjection(statement[1:])

        elif (operator == SELECTION):
            node = NodeSelection(statement[1])

        elif (operator == COUNT):
            node = NodeCount()

        elif (operator == LIMIT):
            node = NodeLimit(statement[1])

        elif (operator == AVERAGE):
            node = NodeAverage()

        elif (operator == FILE_SCAN):
            node = NodeFileScan(statement[1:])

        elif (operator == TEST_SCAN):
            node = NodeTestScan()

        if root_node is None:
            root_node = node
            current_node = node
        else:
            current_node.set_child(node)
            current_node = node

    row = root_node.next()
    while row is not None:
        print(row)
        row = root_node.next()

    root_node.close()

query = [
    [ COUNT ],
    [ PROJECTION, "rating" ],
    [ SELECTION, ["movieId", EQUALS, "5000"]],
    [ FILE_SCAN, "data/ratings.csv" ],
]

process(query)
