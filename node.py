class Node:

    def __init__(self):
        self.children = []

    def set_children(self, input_children):
        for child in input_children:
            if isinstance(child, list):
                node = child[0]
                self.children.append(node)
                node.set_children(child[1:])
            elif isinstance(child, Node):
                self.children.append(child)


    def close(self):
        for child in self.children:
            child.close()

    def next(self):
        self.children[0].next()


