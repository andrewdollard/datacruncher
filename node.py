class Node:

    def set_child(self, child_node):
        self.child = child_node

    def close(self):
        if self.child is not None:
            self.child.close()

