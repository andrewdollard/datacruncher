from constants import *
from node_agg_average import NodeAggAverage
from node_average import NodeAverage
from node_count import NodeCount
from node_file_scan import NodeFileScan
from node_limit import NodeLimit
from node_distinct import NodeDistinct
from node_projection import NodeProjection
from node_selection import NodeSelection
from node_sort import NodeSort
from node_test_scan import NodeTestScan

def process(query):
    current_node = None
    root_node = None

    for node in query:
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
    NodeLimit(10),
    NodeSort('averageRating'),
    NodeAggAverage("rating", "averageRating", ["movieId"]),
    NodeFileScan("data/ratings.csv" ),
]

process(query)
