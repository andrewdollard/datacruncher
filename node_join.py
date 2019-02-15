from constants import *
from node import Node

class NodeJoin(Node):

    def __init__(self, leftCol, condition, rightCol):
        super().__init__()
        self.leftCol = leftCol
        self.condition = condition
        self.rightCol = rightCol

        self.left = None
        self.leftRow = None

    def next(self):
        if not self.left:
            self.left = self.children[0]
            self.right = self.children[1]
            self.leftRow = self.left.next()

        while self.leftRow is not None:

            rightRow = self.right.next()
            while rightRow is not None:
                if self._joinConditionMet(self.leftRow, rightRow):
                    return { **self.leftRow, **rightRow }
                rightRow = self.right.next()

            self.leftRow = self.left.next()
            if self.leftRow is not None:
                self.right.reset()

        return None


    def _joinConditionMet(self, leftRow, rightRow):
        if self.condition == EQUALS:
            return leftRow[self.leftCol] == rightRow[self.rightCol]

