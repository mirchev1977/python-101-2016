class Tree:
    """docstring for Tree"""

    def __init__(self, root):
        self.data = root
        self.children = []

    def add_child(self, root, child):
        if self.root_is_current_tree(root):
            subtree = Tree(child)
            self.children.append(subtree)

    def find_proper_node(self):
        if len(self.children) <= 0:
            return False

    def has_children(self):
        if len(self.children) > 0:
            return True
        return False

    def root_is_current_tree(self, value):
        if value == self.data:
            return True
        else:
            return False

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

