from constants import *
from node import Node
from node_agg_average import NodeAggAverage
from node_average import NodeAverage
from node_count import NodeCount
from node_file_scan import NodeFileScan
from node_join import NodeJoin
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

# q = [NodeLimit(3),
#         [NodeProjection(["title"]),
#             NodeFileScan("data/movies_head.csv")
#     ] ]

# q = [NodeSelection("title", EQUALS, "Jumanji (1995)"),
#         [ NodeJoin("movieId", EQUALS, "movieId"),
#                 NodeFileScan("data/ratings_head.csv"), NodeFileScan("data/movies_head.csv"),
#         ]
#     ]

# q = [ NodeJoin("movieId", EQUALS, "movieId"),
#         NodeFileScan("data/movies_head.csv"), NodeFileScan("data/ratings_head.csv"),
#     ]

q = [ NodeAverage(),
        [ NodeProjection(["rating"]),
            [ NodeJoin("movieId", EQUALS, "movieId"),
                [ NodeSelection("title", EQUALS, "Jumanji (1995)"), NodeFileScan("data/movies_head.csv")],
                NodeFileScan("data/ratings_head.csv"),
            ]
        ]
    ]

process(q)
