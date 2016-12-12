from Node import Node


class Tree:
    """docstring for Tree"""
    def __init__(self, root):
        self.node = Node(list(root), None)

    def solve(self):
        self.create_moves(self.node.root)

    def create_moves(self, parent):
        result = []
        for i in range(len(parent)):
            if parent[i] == '_':
                if parent[i - 1] == '>' and i - 1 >= 0:
                    temp = parent[:]
                    temp[i], temp[i - 1] = temp[i - 1], temp[i]
                    result.append(temp)
                if parent[i - 2] == '>' and i - 2 >= 0:
                    temp = parent[:]
                    temp[i], temp[i - 2] = temp[i - 2], temp[i]
                    result.append(temp)
                if parent[i + 1] == '<' and i + 1 <= len(parent) - 1:
                    temp = parent[:]
                    temp[i], temp[i + 1] = temp[i + 1], temp[i]
                    result.append(temp)
                if parent[i + 2] == '<' and i + 2 <= len(parent) - 1:
                    temp = parent[:]
                    temp[i], temp[i + 2] = temp[i + 2], temp[i]
                    result.append(temp)
        if(len(result) == 0):
            return False
        return result

    def append_children(self):
        pass

