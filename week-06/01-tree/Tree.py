class Tree:
    """docstring for Tree"""

    def __init__(self, root):
        self.data = root
        self.children = []

    def add_child(self, root, child):
        self.children.append(child)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

