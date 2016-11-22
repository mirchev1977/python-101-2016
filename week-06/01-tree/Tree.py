class Tree:
    """docstring for Tree"""

    def __init__(self, root):
        self.data = root
        self.children = []
        self.current_height = 0
        self._height = 0
        self._count = 1

    def add_child(self, root, child):
        self._count += 1
        if self.root_is_current_tree(root):
            subtree = Tree(child)
            self.children.append(subtree)
        else:
            self.find_proper_node(root, child)

    def count_nodes(self):
        return self._count

    def height(self):
        self._height = 0
        self.current_height = 0

        self.current_height += 1
        if self.current_height > self._height:
            self._height = self.current_height

        if len(self.children) <= 0:
            return self._height
        else:
            self.find_height(self.children)

        return self._height

    def find_height(self, children):
        self.current_height += 1
        if self.current_height > self._height:
            self._height = self.current_height

        for tree in children:
            if len(tree.children) > 0:
                self.find_height(tree.children)

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
