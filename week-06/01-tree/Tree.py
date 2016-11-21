class Tree:
    """docstring for Tree"""

    def __init__(self, root):
        self.data = root
        self.children = []

    def add_child(self, root, child):
        if self.root_is_current_tree(root):
            subtree = Tree(child)
            self.children.append(subtree)
        else:
            self.find_proper_node(root, child)

    def find(self, x):
        if self.data == x:
            return True
        elif(len(self.children) > 0):
            return self.__find_in_children(self.children, x)

    def __find_in_children(self, children, x):
        for tree in children:
            if tree.data == x:
                return True
            else:
                if len(tree.children) > 0:
                    result = self.__find_in_children(tree.children, x)
                    if result:
                        return True

        return False

    def find_proper_node(self, root, child):
        if len(self.children) <= 0:
            return False
        self.__find_node_by_value(self.children, root, child)

    def __find_node_by_value(self, children, root, child):
        for current_tree in children:
            if current_tree.data == root:
                current_tree.add_child(root, child)
            else:
                self.__find_node_by_value(
                    current_tree.children, root, child)

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
