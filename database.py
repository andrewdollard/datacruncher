from constants import *
from node import Node
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
    root_node = query[0]
    root_node.set_children(query[1:])

    row = root_node.next()
    while row is not None:
        print(row)
        row = root_node.next()

    root_node.close()


q = [NodeLimit(3),
        [NodeProjection(["title"]),
            NodeFileScan("data/movies_head.csv")
    ] ]

# [NodeSelect("title", EQUALS, "Medium Cool"),
        # [NodeJoin("movieId", EQUALS, "id"), [NodeFileScan("data/ratings.csv"), NodeFileScan("data/movies.csv")] ] ]

process(q)
