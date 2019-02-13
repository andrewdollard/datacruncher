from node import Node

class NodeAggAverage(Node):
    def __init__(self, aggCol, asCol, groupingCols):
        self.aggCol = aggCol
        self.asCol = asCol
        self.groupingCols = groupingCols
        self.runningAvgs = dict()
        self.ran = False
        self.currentIdx = 0

    def next(self):
        if not self.ran:
            row = self.child.next()
            while row is not None:
                groupingKey = tuple([row[k] for k in self.groupingCols])
                if groupingKey in self.runningAvgs.keys():
                    group = self.runningAvgs[groupingKey]
                    group = (group[0] + 1, group[1] + float(row[self.aggCol]))
                else:
                    group = (1, float(row[self.aggCol]))

                self.runningAvgs[groupingKey] = group
                row = self.child.next()
            self.ran = True

        keys = list(self.runningAvgs.keys())
        if self.currentIdx >= len(keys):
            return None

        nextKey = keys[self.currentIdx]
        nextResult = self.runningAvgs[nextKey]
        resultRow = {self.groupingCols[i]: nextKey[i] for i in range(0, len(self.groupingCols))}
        resultRow[self.asCol] = nextResult[1] / nextResult[0]
        self.currentIdx += 1
        return resultRow

